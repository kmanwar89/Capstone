#!/usr/bin/python

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
