## Capstone
JMU Senior Capstone Files Spring 2017

Kadar Anwar & Devon Richards

### Update 11/28/2016
* Files have been updated to reflect changes made on 11/27/2016
  * This includes a working websocket implementation using *websocketd*
  * Files not included are those contained on the Raspberry Pi

### Update 11/29/2016
* Python code files updated in the "Pi Files" folder with comments

##### All files prior to February 2017 have been sorted and deleted. All code has been merged into current mongo.py file

### 2/1/2017
* devon.py - Devon's code for interfacing MongoDB & Python
* mongo.py - Kadar's code for interfacing Python, MongoDB & MQTT. Pulls data
from SenseHAT.

### 2/7/2017
* visualization.html - test file that helps us to understand how data can be
visualized using D3.

### 2/9/2017
* brokercapturefiltered.pcapng - Broker PCAP capture (MongoDB & MQTT)
* clientcapturefiltered.pcapng - Client PCAP capture (Websocket connection)

### 2/10/2017
* Wireshark captures for each of the MQTT client (Pi), MongoDB (on the web server)
and client (websockets).

* Note: Need to re-take captures on Pi in order to be able to view contents of
packets; currently, any use of remote technology (VNC, SSH) masks the data.

* index.html - file that demonstrates the use of Paho JavaScript MQTT library
in order to create connection with MQTT broker.

### 2/12/2017
* Re-organized all files and performed fresh Raspbian install on Raspberry Pi

### 2/13/2017
* Old files removed/re-organized. Only current files used from here on out.
* Removed individual dated folders -- instead, we will update this readme file
with the date, and what was changed during that time.

* http://www.hivemq.com/demos/websocket-client/ -- cool web client for MQTT that
lets us test our configuration from a browser.

* index3.html - code for enabling buttons that connect/disconnect to a topic.
* index3.js - code that matches index3.html and enables button actions.
* index2.html - Source:
http://jpmens.net/2014/07/03/the-mosquitto-mqtt-broker-gets-websockets-support/.
Just another HTML file linking JavaScript, Paho MQTT & HTML.

* Additional Websocket server - Python implementation
* mqtt-panel - another implementation to look at: https://github.com/fabaff/mqtt-panel
* Home automation system we can maybe look into? : https://home-assistant.io/components/mqtt/

### 2/17/2017
* Created Python scripts for stress testing system (clientstress.py & publishstress.py) - KA
* Fixed mqttws31.js file -- had the wrong code in it.  This file is the Paho MQTT JavaScript library file and shouldn't be modified.
* index2.html and Paho's MQTT web client were also tested with our configuration and confirmed as correctly working.
* Website needs to be worked on -- combine the best features from the various examples available to us.

### 2/22/2017
* Devon has Github access and can push/pull files easily
* Both partners worked to figure out message persistence
  * Have to add '-q #' to message while using mosquitto_clients to set QoS value
  * QoS adds 4 packets of overhead per verification
