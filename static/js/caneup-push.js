/**
 * CaneUp Push Client (caneup-push.js)
 * -------------------------------------------------------------
 * Direct Native Web Push Permission Prompt for CaneUp.xyz.
 * Shows the browser's native "Allow / Block" notification prompt
 * directly to the farmer without intermediate popups.
 */

(function() {
  'use strict';

  // Check Web Push & Notification support
  if (!('serviceWorker' in navigator) || !('Notification' in window)) {
    return;
  }

  const STORAGE_KEY = 'caneup_push_state';

  // Inject Styles for Floating Bell Widget
  function injectStyles() {
    if (document.getElementById('caneup-push-styles')) return;
    const style = document.createElement('style');
    style.id = 'caneup-push-styles';
    style.textContent = `
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
      .then((reg) => reg)
      .catch((err) => {
        console.warn('CaneUp SW registration failed:', err);
        return null;
      });
  }

  // Show Welcome Notification immediately upon subscription
  function sendWelcomeNotification(reg) {
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
      if (reg && reg.showNotification) {
        reg.showNotification(title, options);
      } else {
        new Notification(title, options);
      }
    } catch (e) {
      console.log('Welcome notification error:', e);
    }
  }

  // Save subscriber token locally & webhook
  function saveSubscriberToken() {
    try {
      const subscriberInfo = {
        id: 'sub_' + Date.now() + '_' + Math.random().toString(36).substr(2, 9),
        subscribedAt: new Date().toISOString(),
        userAgent: navigator.userAgent,
        platform: navigator.platform || 'Unknown',
        status: 'active'
      };

      const existing = JSON.parse(localStorage.getItem('caneup_push_subscribers') || '[]');
      existing.push(subscriberInfo);
      localStorage.setItem('caneup_push_subscribers', JSON.stringify(existing));

      const webhookUrl = 'https://script.google.com/macros/s/AKfycbw4CHEk9Mi2kPVkrIyC4i0YTpQkG5BSgsNl3mMvdtFYAeSKqKW7_Dmdc_qSZ-qfONz9sA/exec';
      if (webhookUrl) {
        new Image().src = webhookUrl + '?push_sub=1&sub_id=' + encodeURIComponent(subscriberInfo.id) +
                          '&platform=' + encodeURIComponent(subscriberInfo.platform);
      }
    } catch (err) {}
  }

  // Direct Native Permission Request
  let permissionRequested = false;
  function triggerDirectNativePrompt() {
    if (permissionRequested || Notification.permission !== 'default') {
      return;
    }
    permissionRequested = true;

    // Trigger Native Browser Allow/Block Prompt
    Notification.requestPermission().then((permission) => {
      if (permission === 'granted') {
        localStorage.setItem(STORAGE_KEY, 'granted');
        const bell = document.getElementById('caneup-push-bell');
        const badge = document.getElementById('cppBellBadge');
        if (bell) bell.classList.add('subscribed');
        if (badge) badge.textContent = '✓';

        registerServiceWorker().then((reg) => {
          sendWelcomeNotification(reg);
          saveSubscriberToken();
        });

        // Also notify OneSignal SDK if active
        if (window.OneSignal && window.OneSignal.Notifications) {
          try {
            window.OneSignal.Notifications.requestPermission();
          } catch(e) {}
        }
      } else if (permission === 'denied') {
        localStorage.setItem(STORAGE_KEY, 'blocked');
      }
    });
  }

  // Create Floating Bell Widget
  function createBellWidget() {
    if (document.getElementById('caneup-push-bell')) return;
    const bell = document.createElement('div');
    bell.id = 'caneup-push-bell';
    bell.title = '🔔 गन्ना अपडेट्स नोटिफिकेशन';
    bell.innerHTML = `🔔<span class="cpp-badge" id="cppBellBadge">1</span>`;
    document.body.appendChild(bell);

    bell.addEventListener('click', () => {
      if (Notification.permission === 'granted') {
        alert('✅ आप पहले से ही CaneUp नोटिफिकेशन से जुड़े हुए हैं!');
      } else {
        triggerDirectNativePrompt();
      }
    });
  }

  // Initialization Logic
  function init() {
    injectStyles();
    createBellWidget();

    // If already granted, register SW & update bell
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
      return;
    }

    // Direct Native Prompt:
    // 1. Try on page load after 1.5 seconds
    setTimeout(triggerDirectNativePrompt, 1500);

    // 2. Also attach to the very first user interaction (tap, click, scroll)
    // Modern browsers require a user gesture to display the prominent native prompt
    const userGestureEvents = ['click', 'touchstart', 'scroll', 'keydown'];
    function onFirstInteraction() {
      triggerDirectNativePrompt();
      userGestureEvents.forEach((ev) => window.removeEventListener(ev, onFirstInteraction));
    }
    userGestureEvents.forEach((ev) => window.addEventListener(ev, onFirstInteraction, { once: true, passive: true }));
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
