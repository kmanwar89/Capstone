## Various notes

Create a simple web page with the following:
  * 4 protocol types (MQTT, AMQP, STOMP, WebSocket)
  * 4 Radio buttons
  * One text file for send and/or receive
  * One button to initiate connection
    button should call the appropriate javascript file to initiate the connection
    once the button is clicked and the connection is established, query the mongo
    database for the sensor data from the SenseHat

##### Other stuff:
http://www.bogotobogo.com/python/MongoDB_PyMongo/python_MongoDB_RESTAPI_with_Flask.php
https://www.getpostman.com/ - API development platform

* Web servers:
  * Python & flask?
  * nginx
  * python web server
  * fenix

### Example HTML code for Websockets
    <!DOCTYPE html>
    <html>
    <head>
      <title>websocketd count example</title>
      <style>
        #count {
          font: bold 15px arial;
          margin: auto;
          padding: 10px;
          text-align: center;
        }
      </style>
    </head>
    <body>

      <div id="count"></div>

      <script>
        var ws = new WebSocket('ws://192.168.99.120:8080/');
        ws.onopen = function() {
          document.body.style.backgroundColor = '#cfc';
        };
        ws.onclose = function() {
          document.body.style.backgroundColor = null;
        };
        ws.onmessage = function(event) {
          document.getElementById('count').textContent = event.data;
        };
      </script>

    </body>
  </html>
