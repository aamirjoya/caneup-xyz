/**
 * CaneUp Push Client (caneup-push.js)
 * -------------------------------------------------------------
 * Custom, high-CTR LaraPush-style web push notification manager.
 * Features:
 * - High-converting Hindi 2-step soft ask opt-in prompt
 * - Floating notification bell with unread badge
 * - Instant rich welcome notification
 * - Automatic Service Worker registration
 * - Offline & mobile-optimized
 */

(function() {
  'use strict';

  // Check Web Push & Notification support
  if (!('serviceWorker' in navigator) || !('Notification' in window)) {
    return;
  }

  const STORAGE_KEY = 'caneup_push_state'; // 'granted', 'dismissed', 'blocked'
  const DISMISS_TIMEOUT = 24 * 60 * 60 * 1000; // Ask again after 24 hours if dismissed
  const DISMISS_TIMESTAMP_KEY = 'caneup_push_dismiss_time';

  // Inject CSS Styles for LaraPush Prompt & Floating Bell
  function injectStyles() {
    if (document.getElementById('caneup-push-styles')) return;
    const style = document.createElement('style');
    style.id = 'caneup-push-styles';
    style.textContent = `
      /* LaraPush Style Slide-down Prompt */
      #caneup-push-prompt {
        position: fixed;
        bottom: 24px;
        right: 24px;
        width: calc(100% - 32px);
        max-width: 420px;
        background: #ffffff;
        border-radius: 16px;
        box-shadow: 0 12px 40px rgba(0, 0, 0, 0.22), 0 2px 10px rgba(21, 128, 61, 0.12);
        border: 1.5px solid #86efac;
        padding: 20px;
        z-index: 999999;
        font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Noto Sans Devanagari', sans-serif;
        transform: translateY(120%);
        opacity: 0;
        transition: transform 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275), opacity 0.3s ease;
      }
      #caneup-push-prompt.active {
        transform: translateY(0);
        opacity: 1;
      }
      .cpp-header {
        display: flex;
        align-items: flex-start;
        gap: 14px;
        margin-bottom: 14px;
      }
      .cpp-icon-wrap {
        width: 48px;
        height: 48px;
        background: linear-gradient(135deg, #15803d, #166534);
        border-radius: 12px;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 24px;
        color: #ffffff;
        flex-shrink: 0;
        box-shadow: 0 4px 12px rgba(21, 128, 61, 0.35);
        animation: cpp-bell-pulse 2s infinite ease-in-out;
      }
      @keyframes cpp-bell-pulse {
        0%, 100% { transform: scale(1) rotate(0deg); }
        15% { transform: scale(1.1) rotate(-10deg); }
        30% { transform: scale(1.1) rotate(10deg); }
        45% { transform: scale(1) rotate(0deg); }
      }
      .cpp-title {
        font-size: 15px;
        font-weight: 800;
        color: #111827;
        margin: 0 0 4px;
        line-height: 1.35;
      }
      .cpp-desc {
        font-size: 13px;
        color: #4b5563;
        margin: 0;
        line-height: 1.5;
      }
      .cpp-actions {
        display: flex;
        gap: 10px;
        margin-top: 14px;
      }
      .cpp-btn-allow {
        flex: 1.3;
        background: linear-gradient(135deg, #15803d, #166534);
        color: #ffffff;
        border: none;
        border-radius: 10px;
        padding: 11px 16px;
        font-size: 13px;
        font-weight: 700;
        cursor: pointer;
        display: inline-flex;
        align-items: center;
        justify-content: center;
        gap: 6px;
        box-shadow: 0 4px 12px rgba(21, 128, 61, 0.3);
        transition: transform 0.15s ease, background 0.2s ease;
      }
      .cpp-btn-allow:hover {
        background: #14532d;
        transform: translateY(-1px);
      }
      .cpp-btn-dismiss {
        flex: 0.8;
        background: #f3f4f6;
        color: #6b7280;
        border: 1px solid #e5e7eb;
        border-radius: 10px;
        padding: 11px 12px;
        font-size: 13px;
        font-weight: 600;
        cursor: pointer;
        transition: background 0.2s ease;
      }
      .cpp-btn-dismiss:hover {
        background: #e5e7eb;
        color: #374151;
      }

      /* Floating Bell Widget */
      #caneup-push-bell {
        position: fixed;
        bottom: 24px;
        left: 24px;
        width: 48px;
        height: 48px;
        border-radius: 50%;
        background: #ffffff;
        box-shadow: 0 4px 16px rgba(0, 0, 0, 0.18), 0 0 0 2px #86efac;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 22px;
        cursor: pointer;
        z-index: 999990;
        transition: transform 0.25s cubic-bezier(0.175, 0.885, 0.32, 1.275);
      }
      #caneup-push-bell:hover {
        transform: scale(1.12);
      }
      #caneup-push-bell .cpp-badge {
        position: absolute;
        top: -3px;
        right: -3px;
        width: 18px;
        height: 18px;
        background: #ef4444;
        color: #ffffff;
        font-size: 10px;
        font-weight: 800;
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        border: 2px solid #ffffff;
      }
      #caneup-push-bell.subscribed .cpp-badge {
        background: #22c55e;
      }

      @media (max-width: 640px) {
        #caneup-push-prompt {
          bottom: 16px;
          right: 16px;
          left: 16px;
          width: auto;
          padding: 16px;
        }
        #caneup-push-bell {
          bottom: 16px;
          left: 16px;
          width: 42px;
          height: 42px;
          font-size: 20px;
        }
      }
    `;
    document.head.appendChild(style);
  }

  // Register Service Worker
  function registerServiceWorker() {
    return navigator.serviceWorker.register('/caneup-sw.js', { scope: '/' })
      .then((reg) => {
        return reg;
      })
      .catch((err) => {
        console.warn('CaneUp SW registration failed:', err);
        return null;
      });
  }

  // Show Welcome Notification immediately upon subscription
  function sendWelcomeNotification(reg) {
    if (!reg) return;
    const title = '🎉 CaneUp किसान सेवा से जुड़ने के लिए धन्यवाद!';
    const options = {
      body: 'अब आपको गन्ना पर्ची, सट्टा संशोधन व भुगतान के दैनिक जरूरी अपडेट्स सीधे मिलते रहेंगे।',
      icon: '/images/logo-192.png',
      badge: '/images/favicon-32x32.png',
      vibrate: [150, 80, 150],
      tag: 'caneup-welcome',
      data: {
        url: 'https://caneup.xyz/'
      }
    };
    try {
      reg.showNotification(title, options);
    } catch (e) {
      new Notification(title, options);
    }
  }

  // Create & Inject HTML DOM for Prompt and Floating Bell
  function createPromptElements() {
    // Prompt Box
    const prompt = document.createElement('div');
    prompt.id = 'caneup-push-prompt';
    prompt.innerHTML = `
      <div class="cpp-header">
        <div class="cpp-icon-wrap">🔔</div>
        <div>
          <div class="cpp-title">गन्ना पर्ची, सट्टा व रेट्स के लाइव अलर्ट!</div>
          <div class="cpp-desc">क्या आप आज की पर्ची, सट्टा संशोधन, और ताज़ा गन्ना भाव के लाइव नोटिफिकेशन पाना चाहते हैं?</div>
        </div>
      </div>
      <div class="cpp-actions">
        <button class="cpp-btn-allow" id="cppAllowBtn">
          <span>🔔 हाँ, नोटिफिकेशन चालू करें</span>
        </button>
        <button class="cpp-btn-dismiss" id="cppDismissBtn">बाद में</button>
      </div>
    `;
    document.body.appendChild(prompt);

    // Floating Bell Widget
    const bell = document.createElement('div');
    bell.id = 'caneup-push-bell';
    bell.title = '🔔 गन्ना अपडेट्स नोटिफिकेशन';
    bell.innerHTML = `🔔<span class="cpp-badge" id="cppBellBadge">1</span>`;
    document.body.appendChild(bell);

    // Event Handlers
    document.getElementById('cppAllowBtn').addEventListener('click', onAllowClick);
    document.getElementById('cppDismissBtn').addEventListener('click', onDismissClick);
    bell.addEventListener('click', () => {
      prompt.classList.add('active');
    });
  }

  // On "हाँ, नोटिफिकेशन चालू करें" Click
  function onAllowClick() {
    const prompt = document.getElementById('caneup-push-prompt');
    const allowBtn = document.getElementById('cppAllowBtn');
    if (allowBtn) allowBtn.textContent = '⏳ एक्टिवेट हो रहा है...';

    Notification.requestPermission().then((permission) => {
      if (permission === 'granted') {
        localStorage.setItem(STORAGE_KEY, 'granted');
        if (prompt) prompt.classList.remove('active');

        // Update bell
        const bell = document.getElementById('caneup-push-bell');
        const badge = document.getElementById('cppBellBadge');
        if (bell) bell.classList.add('subscribed');
        if (badge) badge.textContent = '✓';

        // Register SW & send welcome notification
        registerServiceWorker().then((reg) => {
          sendWelcomeNotification(reg);
          saveSubscriberToken(reg);
        });
      } else if (permission === 'denied') {
        localStorage.setItem(STORAGE_KEY, 'blocked');
        if (prompt) prompt.classList.remove('active');
      } else {
        localStorage.setItem(STORAGE_KEY, 'dismissed');
        localStorage.setItem(DISMISS_TIMESTAMP_KEY, Date.now().toString());
        if (prompt) prompt.classList.remove('active');
      }
    });
  }

  // On "बाद में" Click
  function onDismissClick() {
    const prompt = document.getElementById('caneup-push-prompt');
    if (prompt) prompt.classList.remove('active');
    localStorage.setItem(STORAGE_KEY, 'dismissed');
    localStorage.setItem(DISMISS_TIMESTAMP_KEY, Date.now().toString());
  }

  // Save subscriber endpoint/token locally and sync to storage
  function saveSubscriberToken(reg) {
    try {
      const subscriberInfo = {
        id: 'sub_' + Date.now() + '_' + Math.random().toString(36).substr(2, 9),
        subscribedAt: new Date().toISOString(),
        userAgent: navigator.userAgent,
        platform: navigator.platform || 'Unknown',
        language: navigator.language || 'hi',
        status: 'active'
      };

      const existing = JSON.parse(localStorage.getItem('caneup_push_subscribers') || '[]');
      existing.push(subscriberInfo);
      localStorage.setItem('caneup_push_subscribers', JSON.stringify(existing));

      // Dual Background Sync to Google Sheets / Webhook if configured
      const webhookUrl = 'https://script.google.com/macros/s/AKfycbw4CHEk9Mi2kPVkrIyC4i0YTpQkG5BSgsNl3mMvdtFYAeSKqKW7_Dmdc_qSZ-qfONz9sA/exec';
      if (webhookUrl) {
        new Image().src = webhookUrl + '?push_sub=1&sub_id=' + encodeURIComponent(subscriberInfo.id) +
                          '&platform=' + encodeURIComponent(subscriberInfo.platform);
      }
    } catch (err) {
      console.warn('Error saving subscriber info:', err);
    }
  }

  // Initialization Logic
  function init() {
    injectStyles();
    createPromptElements();

    // If already granted, register SW and update bell
    if (Notification.permission === 'granted') {
      localStorage.setItem(STORAGE_KEY, 'granted');
      const bell = document.getElementById('caneup-push-bell');
      const badge = document.getElementById('cppBellBadge');
      if (bell) bell.classList.add('subscribed');
      if (badge) badge.textContent = '✓';
      registerServiceWorker();
      return;
    }

    if (Notification.permission === 'denied') {
      return; // Respect user rejection
    }

    // Check dismissed cooldown
    const state = localStorage.getItem(STORAGE_KEY);
    const dismissTime = parseInt(localStorage.getItem(DISMISS_TIMESTAMP_KEY) || '0', 10);
    const now = Date.now();

    if (state === 'dismissed' && (now - dismissTime) < DISMISS_TIMEOUT) {
      return; // Within 24-hour cooldown
    }

    // Show prompt after 3.5 seconds of browsing
    setTimeout(() => {
      const prompt = document.getElementById('caneup-push-prompt');
      if (prompt && Notification.permission !== 'granted') {
        prompt.classList.add('active');
      }
    }, 3500);
  }

  // Load after DOM is ready
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
