#!/usr/bin/python

# MQTT Publish

# Purpose: Import sensor data from SenseHAT and publish to broker via MQTT

# Author: Kadar M. Anwar
# Language: Python 3.5
# Date: 2-22-2017
# JMU ISAT Senior Capstone Project

# v0.1 - 2/22/2017 - initial code
# v0.2 - 2/23/2017 - combining code from publish2.py and publish.py into a single file

# Import libraries
from sense_hat import SenseHat
import paho.mqtt.client as mqtt
import time

# Instantiate objects
client = mqtt.Client()
sense = SenseHat()

# Connect to the broker over MQTT port
client.connect("192.168.99.75", port=1883, keepalive=60)
client.loop_start() # Keep the connection open

# Get temperature from sensor and convert it to Farenheit
tempC = sense.get_temperature()
tempF = (tempC * 1.8) + 32
#tempF = format('.2f', tempF)

# Publish a message to the "Capstone" topic
client.publish("Capstone", payload=tempF, qos=0)

while True:
    client.publish("Capstone", payload = tempF, qos=0)
	# (rc, mid) = client.publish("Capstone", payload=tempF, qos=0)
    time.sleep(1)

############################################
# Additional callbacks, not used currently #
############################################
# def on_publish(client, userdata, mid):
#     print("mid: "+str(mid))
#def on_connect(client, userdata, rc):
#    print("Connection Result: "+connack_string(rc))
#client.on_publish = on_publish
#client.on_connect = on_connect


#	humidity = sense.get_humidity()
#	pressure = sense.get_pressure()
#	psi = (pressure * 0.0145038)



#    time.sleep(30)
    #temperature = read_from_imaginary_thermometer()
################





# Keep the connection open
#client.loop_forever()

# disconnect
#client.disconnect()

# while True:
#     client = new MqttClient("tcp://192.168.99.71:1883", "ClientIdentifier");
#     client.connect();
#     MqttMessage message = new MqttMessage();
#     message.setPayload("A single message".getBytes());
#     client.publish("Capstone", message);
#client.disconnect();


# SSL/TLS support, not currently used.
# tls_set(ca_certs, certfile=None, keyfile=None, cert_reqs=ssl.CERT_REQUIRED,
#     tls_version=ssl.PROTOCOL_TLSv1, ciphers=None)

## Interesting function we may be able to use in our vulnerability
# scenarios
# tls_insecure_set()
#
# tls_insecure_set(value)
# Configure verification of the server hostname in the server certificate.
#
# If value is set to True, it is impossible to guarantee that the host you are connecting to is not impersonating your server. This can be useful in initial server testing, but makes it possible for a malicious third party to impersonate your server through DNS spoofing, for example.
#
# Do not use this function in a real system. Setting value to True means there is no point using encryption.
#
# Must be called before connect*).
