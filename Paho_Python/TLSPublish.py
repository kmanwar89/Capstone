#!/usr/bin/python

# Purpose: Import sensor data from SenseHAT and publish to broker via MQTT

# Author: Kadar M. Anwar
# Language: Python 3.5
# Date: 2-22-2017
# JMU ISAT Senior Capstone Project

# v0.1 - 2/22/2017 - initial code
# v0.2 - 2/23/2017 - combining code from publish2.py and publish.py into a single file
# v0.3 - 4/14/2017 - updating code for Dry Run #2, combined data gathering
#	and temp conversion with formatting into a single string.
#	Fixed values not updating in real-time.

# Import libraries
from sense_hat import SenseHat
import paho.mqtt.client as mqtt
import time

# Instantiate objects
client = mqtt.Client()
sense = SenseHat()

# Connect to the broker over MQTT port
client.username_pw_set("admin", "admin")
client.tls_set("ca.crt")
client.connect("192.168.99.75", port=8883, keepalive=60)
client.loop_start() # Keep the connection open


# Publish a message to the "Capstone" topic
running = True
while running:

	# Get temperature from sensor and convert it to Farenheit
	tempF = format(((sense.get_temperature() * 1.8) + 32), '.2f')
	humidity = format(sense.get_humidity(), '.2f')
	psi = format(sense.get_pressure() * 0.0145038, '.2f')

	# Send multiple values as a dictionary
	data = {'Temperature (Farenheit)':tempF,'Humidity (% relative)':humidity,'Pressure (psi)':psi}

	# Publish the message to the Capstone topic
	client.publish("Capstone", payload = str(data), qos=0)


#	data = {'tempC':sense.get_temperature(), 'humidity':sense.get_humidity()}
#+	msgs=[{'topic':"Capstone", 'payload':"The temperature is now"+" "\
#		 + format(tempC, '.2f')+" degrees F"}]

#print("Current environmental conditions:" \
#		+ ' ' + "Temperature:" + str(tempF) \
#		+ ' ' + "% Relative Humidity" + str(humidity) \
#		+ ' ' + "Pressure (PSI)" + str(psi))
#    client.publish("Capstone", payload = tempF, qos=0)
