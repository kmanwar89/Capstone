#!/usr/bin/python

# MQTT Publish Stress Test

# Purpose: Stress test MQTT broker with publishing thousands of messages.

# Author: Kadar M. Anwar
# Language: Python 3.5
# Date: 2-23-2017
# JMU ISAT Senior Capstone Project

# v0.1 - 2/23/2017 - initial code
# v0.2 - 4/9/2017 - Modified code to remove SenseHat code, since the stress test would be conducted on a desktop or laptop, not the sensor.

# Import libraries
import paho.mqtt.client as mqtt
import time

# Define variables
host = ''

# Instantiate objects
client = mqtt.Client()

# Get the IP address from the user
#host = input('Please enter the IP address of the broker you wish to test')

# Connect to the broker over MQTT port
#client.connect(host, port=1883, keepalive=60)
client.username_pw_set(admin, password=admin)
client.connect("192.168.99.135", port=1883, keepalive=60)
client.loop_start() # Keep the connection open

# Get temperature from sensor and convert it to Farenheit
tempC = sense.get_temperature()
tempF = (tempC * 1.8) + 32
#tempF = format('.2f', tempF)

# Publish a message to the "Capstone" topic
#client.publish("Capstone", payload=tempF, qos=0)

# Loop the stress test
z = 0
for x in range(0,1001):
	for y in range (0,101):
		client.publish("Capstone", payload = tempF, qos=0)
		z+=1
		print(z, "packets sent")

#print("Packets sent successfully: ", x*y)
#print("Packets sent total: ", z)
