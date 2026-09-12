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

  // Create Floating Bell Widget
  function createBellWidget() {
    if (document.getElementById('caneup-push-bell')) return;
    const bell = document.createElement('div');
    bell.id = 'caneup-push-bell';
    bell.title = '🔔 गन्ना अपडेट्स नोटिफिकेशन';
    bell.innerHTML = `🔔<span class="cpp-badge" id="cppBellBadge">1</span>`;
    document.body.appendChild(bell);

    bell.addEventListener('click', () => {
      if (typeof Notification !== 'undefined' && Notification.permission === 'granted') {
        alert('✅ आप पहले से ही CaneUp लाइव नोटिफिकेशन से जुड़े हुए हैं!');
      } else {
        window.OneSignalDeferred = window.OneSignalDeferred || [];
        window.OneSignalDeferred.push(async function(OneSignal) {
          try {
            await OneSignal.Notifications.requestPermission();
          } catch(e) {}
        });
      }
    });
  }

  // Connect to OneSignal SDK lifecycle
  function connectOneSignal() {
    window.OneSignalDeferred = window.OneSignalDeferred || [];
    window.OneSignalDeferred.push(function(OneSignal) {
      // Check initial state
      const isPushEnabled = OneSignal.User && OneSignal.User.PushSubscription && OneSignal.User.PushSubscription.optedIn;
      if (isPushEnabled || (typeof Notification !== 'undefined' && Notification.permission === 'granted')) {
        updateBellStatus(true);
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
