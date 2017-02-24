#!/usr/bin/python

# MQTT Publish

# Purpose: Attempting to figure out syntax for publishing messages
# without initiating a TCP 4-way close after each message.

# Author: Kadar M. Anwar
# Language: Python 3.5
# Date: 2-22-2017
# JMU ISAT Senior Capstone Project

from sense_hat import SenseHat
import paho.mqtt.client as mqtt

# Instantiate a Client object from the MQTT library
client = mqtt.Client()

sense = SenseHat()

# Connect to the broker
client.connect("192.168.99.75", port=1883, keepalive=60)

tempC = sense.get_temperature()
tempF = (tempC * 1.8) + 32
#	humidity = sense.get_humidity()
#	pressure = sense.get_pressure()
#	psi = (pressure * 0.0145038)

# Publish a message
client.publish("Capstone", payload=tempF, qos=0)

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
