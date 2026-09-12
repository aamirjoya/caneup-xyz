/**
 * CaneUp Push Client (caneup-push.js)
 * -------------------------------------------------------------
 * Custom UI and helper for CaneUp Push Notifications.
 * Integrates directly with OneSignal v16 SDK:
 * - Floating notification bell with live subscription status
 * - Listens for OneSignal opt-in events
 * - Instant rich welcome notification on permission grant
 * - Zero service worker conflicts
 */

(function() {
  'use strict';

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

      /* iOS PWA Instruction Sheet */
      #caneup-ios-sheet {
        position: fixed;
        inset: 0;
        z-index: 999999;
        display: flex;
        align-items: flex-end;
        justify-content: center;
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
      }
      .caneup-ios-overlay {
        position: absolute;
        inset: 0;
        background: rgba(0, 0, 0, 0.55);
        backdrop-filter: blur(3px);
        -webkit-backdrop-filter: blur(3px);
      }
      .caneup-ios-card {
        position: relative;
        background: #ffffff;
        width: 100%;
        max-width: 460px;
        border-radius: 24px 24px 0 0;
        padding: 24px 20px 30px;
        box-shadow: 0 -8px 32px rgba(0, 0, 0, 0.22);
        animation: caneupSlideUp 0.3s cubic-bezier(0.16, 1, 0.3, 1);
      }
      @keyframes caneupSlideUp {
        from { transform: translateY(100%); }
        to { transform: translateY(0); }
      }
      .caneup-ios-header {
        display: flex;
        align-items: center;
        justify-content: space-between;
        margin-bottom: 12px;
      }
      .caneup-ios-title {
        display: flex;
        align-items: center;
        gap: 10px;
        font-size: 17px;
        font-weight: 700;
        color: #111827;
      }
      .caneup-ios-close {
        background: #f3f4f6;
        border: none;
        width: 28px;
        height: 28px;
        border-radius: 50%;
        font-size: 18px;
        color: #4b5563;
        cursor: pointer;
        display: flex;
        align-items: center;
        justify-content: center;
        line-height: 1;
      }
      .caneup-ios-p {
        font-size: 13.5px;
        color: #4b5563;
        line-height: 1.5;
        margin-bottom: 16px;
      }
      .caneup-ios-step-box {
        display: flex;
        flex-direction: column;
        gap: 10px;
        margin-bottom: 20px;
      }
      .caneup-ios-step {
        display: flex;
        align-items: flex-start;
        gap: 12px;
        background: #f8fafc;
        border: 1px solid #e2e8f0;
        padding: 10px 14px;
        border-radius: 12px;
        font-size: 13.5px;
        color: #1e293b;
        line-height: 1.45;
      }
      .step-badge {
        width: 24px;
        height: 24px;
        background: #15803d;
        color: #ffffff;
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 12px;
        font-weight: 700;
        flex-shrink: 0;
      }
      .caneup-ios-confirm {
        width: 100%;
        background: #15803d;
        color: #ffffff;
        border: none;
        padding: 13px;
        font-size: 15px;
        font-weight: 600;
        border-radius: 12px;
        cursor: pointer;
        transition: background 0.2s;
      }
      .caneup-ios-confirm:hover {
        background: #166534;
      }
    `;
    document.head.appendChild(style);
  }

  // Show Welcome Notification on permission grant
  function showWelcomeNotification() {
    if (Notification.permission !== 'granted') return;
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
      if (navigator.serviceWorker && navigator.serviceWorker.ready) {
        navigator.serviceWorker.ready.then((reg) => {
          reg.showNotification(title, options);
        });
      } else {
        new Notification(title, options);
      }
    } catch (e) {}
  }

  // Update Bell Status
  function updateBellStatus(isSubscribed) {
    const bell = document.getElementById('caneup-push-bell');
    const badge = document.getElementById('cppBellBadge');
    if (bell && badge) {
      if (isSubscribed) {
        bell.classList.add('subscribed');
        badge.textContent = '✓';
        bell.title = '✅ CaneUp लाइव नोटिफिकेशन सक्रिय है';
      } else {
        bell.classList.remove('subscribed');
        badge.textContent = '1';
        bell.title = '🔔 गन्ना अपडेट्स नोटिफिकेशन चालू करें';
      }
    }
  }

  // Helper to detect iOS and standalone PWA
  function checkIOS() {
    const isIOS = /iPad|iPhone|iPod/.test(navigator.userAgent) || (navigator.platform === 'MacIntel' && navigator.maxTouchPoints > 1);
    const isStandalone = window.navigator.standalone === true || window.matchMedia('(display-mode: standalone)').matches;
    return { isIOS, isStandalone };
  }

  // Show iOS Step-by-Step Bottom Sheet
  function showIOSInstructions() {
    if (document.getElementById('caneup-ios-sheet')) return;
    const sheet = document.createElement('div');
    sheet.id = 'caneup-ios-sheet';
    sheet.innerHTML = `
      <div class="caneup-ios-overlay" id="caneupIosOverlay"></div>
      <div class="caneup-ios-card">
        <div class="caneup-ios-header">
          <div class="caneup-ios-title">
            <span style="font-size:22px">🍎</span>
            <strong>iPhone पर नोटिफिकेशन चालू करें</strong>
          </div>
          <button type="button" class="caneup-ios-close" id="caneupIosCloseBtn">&times;</button>
        </div>
        <p class="caneup-ios-p">Apple की सुरक्षा नीति के अनुसार iPhone पर नोटिफिकेशन पाने के लिए CaneUp को होम स्क्रीन पर जोड़ना आवश्यक है:</p>
        <div class="caneup-ios-step-box">
          <div class="caneup-ios-step">
            <div class="step-badge">1</div>
            <div>नीचे Safari बार में <strong>Share</strong> बटन ( <svg style="display:inline-block;vertical-align:middle" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 12v8a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2v-8"/><polyline points="16 6 12 2 8 6"/><line x1="12" y1="2" x2="12" y2="15"/></svg> ) दबाएं।</div>
          </div>
          <div class="caneup-ios-step">
            <div class="step-badge">2</div>
            <div>नीचे स्क्रॉल करके <strong>"Add to Home Screen"</strong> (होम स्क्रीन में जोड़ें) चुनें।</div>
          </div>
          <div class="caneup-ios-step">
            <div class="step-badge">3</div>
            <div>अब अपने iPhone की होम स्क्रीन से <strong>CaneUp</strong> खोलें और <strong>Allow</strong> करें!</div>
          </div>
        </div>
        <button type="button" class="caneup-ios-confirm" id="caneupIosOkBtn">समझ गया, ठीक है ✓</button>
      </div>
    `;
    document.body.appendChild(sheet);

    const close = () => {
      if (sheet && sheet.parentNode) sheet.parentNode.removeChild(sheet);
    };
    document.getElementById('caneupIosCloseBtn')?.addEventListener('click', close);
    document.getElementById('caneupIosOverlay')?.addEventListener('click', close);
    document.getElementById('caneupIosOkBtn')?.addEventListener('click', close);
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
      const { isIOS, isStandalone } = checkIOS();
      if (isIOS && !isStandalone) {
        showIOSInstructions();
        return;
      }
      window.OneSignalDeferred = window.OneSignalDeferred || [];
      window.OneSignalDeferred.push(async function(OneSignal) {
        try {
          await OneSignal.User.PushSubscription.optIn();
          if (typeof Notification !== 'undefined' && Notification.permission === 'granted') {
            updateBellStatus(true);
          }
        } catch(e) {
          console.warn('OneSignal optIn error:', e);
        }
      });
    });
  }

  // Cleanup legacy conflicting service worker if cached in visitor's browser
  function cleanupLegacySW() {
    if ('serviceWorker' in navigator) {
      navigator.serviceWorker.getRegistrations().then(function(registrations) {
        for (var i = 0; i < registrations.length; i++) {
          var reg = registrations[i];
          if (reg.active && reg.active.scriptURL && reg.active.scriptURL.indexOf('caneup-sw.js') !== -1) {
            reg.unregister().then(function(unregistered) {
              if (unregistered) {
                console.log('Legacy SW caneup-sw.js unregistered successfully');
              }
            });
          }
        }
      }).catch(function() {});
    }
  }

  // Connect to OneSignal SDK lifecycle
  function connectOneSignal() {
    window.OneSignalDeferred = window.OneSignalDeferred || [];
    window.OneSignalDeferred.push(async function(OneSignal) {
      // Check initial state
      const isPushEnabled = OneSignal.User && OneSignal.User.PushSubscription && OneSignal.User.PushSubscription.optedIn;
      if (isPushEnabled) {
        updateBellStatus(true);
      } else if (typeof Notification !== 'undefined' && Notification.permission === 'granted') {
        // Permission was granted, ensure OneSignal registers the subscriber
        try {
          await OneSignal.User.PushSubscription.optIn();
          updateBellStatus(true);
        } catch (e) {}
      }

      // Listen for subscription changes
      try {
        OneSignal.User.PushSubscription.addEventListener('change', function(changeEvent) {
          if (changeEvent.current && changeEvent.current.optedIn) {
            console.log('OneSignal Push Subscribed successfully! ID:', changeEvent.current.id);
            updateBellStatus(true);
            showWelcomeNotification();
          }
        });
      } catch (err) {}
    });
  }

  function init() {
    cleanupLegacySW();
    injectStyles();
    createBellWidget();
    connectOneSignal();
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
