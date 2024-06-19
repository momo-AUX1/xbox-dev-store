if ('serviceWorker' in navigator) {
            navigator.serviceWorker.register('/static/js/service-worker.js')
            .then(function(registration) {
                console.log('ServiceWorker registration successful with scope: ', registration.scope);
            }, function(error) {
                console.log('ServiceWorker registration failed: ', error);
            });
        }