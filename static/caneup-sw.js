/**
 * CaneUp Web Push Service Worker (caneup-sw.js)
 * -------------------------------------------------------------
 * Custom, self-hosted web push notification handler for CaneUp.xyz.
 * Supports rich banner images, vibration, custom action buttons,
 * tag management, and smart deep-linking.
 */

const SW_VERSION = 'caneup-sw-v1.0.0';

self.addEventListener('install', (event) => {
  self.skipWaiting();
});

self.addEventListener('activate', (event) => {
  event.waitUntil(self.clients.claim());
});

// Handle incoming Web Push notification
self.addEventListener('push', (event) => {
  let data = {};
  if (event.data) {
    try {
      data = event.data.json();
    } catch (e) {
      data = {
        title: 'CaneUp — गन्ना किसान अलर्ट',
        body: event.data.text(),
        url: 'https://caneup.xyz/'
      };
    }
  } else {
    data = {
      title: 'CaneUp — ताज़ा अपडेट',
      body: 'गन्ना पर्ची, सट्टा व भुगतान से जुड़ी नई जानकारी उपलब्ध है।',
      url: 'https://caneup.xyz/'
    };
  }

  const title = data.title || 'CaneUp — गन्ना किसान पोर्टल';
  const options = {
    body: data.body || 'नया अपडेट देखने के लिए क्लिक करें।',
    icon: data.icon || '/images/logo-192.png',
    badge: data.badge || '/images/favicon-32x32.png',
    image: data.image || null,
    vibrate: [200, 100, 200],
    tag: data.tag || 'caneup-news-' + Date.now(),
    renotify: true,
    requireInteraction: data.requireInteraction !== false,
    data: {
      url: data.url || 'https://caneup.xyz/',
      dateOfArrival: Date.now()
    },
    actions: data.actions || [
      { action: 'open_url', title: '👉 अभी देखें' },
      { action: 'dismiss', title: 'बंद करें' }
    ]
  };

  event.waitUntil(
    self.registration.showNotification(title, options)
  );
});

// Handle Notification Clicks (Smart deep linking & window focusing)
self.addEventListener('notificationclick', (event) => {
  event.notification.close();

  const action = event.action;
  if (action === 'dismiss') {
    return;
  }

  const targetUrl = (event.notification.data && event.notification.data.url)
    ? event.notification.data.url
    : 'https://caneup.xyz/';

  event.waitUntil(
    clients.matchAll({ type: 'window', includeUncontrolled: true }).then((windowClients) => {
      // Check if target URL or domain tab is already open
      for (let client of windowClients) {
        if (client.url === targetUrl && 'focus' in client) {
          return client.focus();
        }
      }
      // If not, open new window
      if (clients.openWindow) {
        return clients.openWindow(targetUrl);
      }
    })
  );
});
