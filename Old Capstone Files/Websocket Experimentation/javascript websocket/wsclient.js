var WebSocket = require('ws')
  , ws = new WebSocket('ws://localhost:9000');
ws.on('open', function() {
    ws.send('Client Test');
});
ws.on('message', function(message) {
    console.log('received: %s', message);
});
