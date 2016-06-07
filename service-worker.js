// ---
// layout: null
//---

self.addEventListener('install', function(event) {
  event.waitUntil(
    caches.open('np-v1').then(function(cache) {
      return cache.addAll([
        '/',
        '/css/main.css',
        '/js/ga-events.js',
        'https://ajax.googleapis.com/ajax/libs/jquery/1.12.2/jquery.min.js',
        'https://cdnjs.cloudflare.com/ajax/libs/balance-text/1.6.0/jquery.balancetext.min.js',
        'https://fonts.googleapis.com/css?family=Open+Sans:700,300|Lustria',
        'https://fonts.gstatic.com/s/lustria/v4/P1zvvbOqCVCJzgypDg3MKw.woff2',
        'https://fonts.gstatic.com/s/opensans/v13/DXI1ORHCpsQm3Vp6mXoaTegdm0LZdjqr5-oayXSOefg.woff2',
        'https://fonts.gstatic.com/s/opensans/v13/k3k702ZOKiLJc3WVjuplzOgdm0LZdjqr5-oayXSOefg.woff2',
        '/js/loadRemainingContent.js',
        '/index-data.json'
      ]);
    })
  );
});

self.addEventListener('fetch', function(event) {
  event.respondWith(
    caches.match(event.request).then(function(response) {
      //console.log("getting ", event.request, response);
      return response || fetch(event.request);
    })
  );
});