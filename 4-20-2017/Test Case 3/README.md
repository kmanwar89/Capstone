Screenshot of base64 encoded text (and a text file), along with a wireshark cap
ture showing MQTT packets being published


encode.py contains code to read the JPG file as bytes, encode the bytes to Base64
and publish the message to broker while also printing the output in a terminal
(Note: the b' and ' characters at the beginning and end are /not/ sent via MQTT
so there is no need to remove them for MQTT purposes)

4-20-2017
Encode.py correctly accepts inputs of broker IP address, topic and filename to
encode as base64.


Flow
----
Send image from Camera to Raspberry Pi via FTP
Raspberry Pi stores the image in a new folder with a date and time stamp
Python encode script needs to locate the most recently changed file and perform the encode/transmission via MQTT on it
File is encoded using base64 and sent via MQTT to the broker, which forwards it to the subscriber
  Consequently, this raw data transmission is also visible by another malicious user who is able to subscribe to the same topic using the username/password sniffed in test case 1
  This "partner" is able to decode the MQTT transmission using the 'decode.py' script, which subscribes to the same topic that the Pi is sending the encoded image to, and when it receives a message it runs the bas64 encoding through a decoding process and outputs the image as a jpeg on the receiving computer.
Subscriber is able to view the decoded image on their browser through the use of a JavaScript decode function.







Intercept this transmission wireless using Wireshark (malicious user)
