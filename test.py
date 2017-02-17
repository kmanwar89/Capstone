#!/usr/bin/python

# Quick test file figuring out why MQTT doesn't work in web browser as of
# 2-16-2017

# Author: Kadar M. Anwar
# Language: Python 3.5
# JMU ISAT Senior Capstone Project

# Import required libraries
from sense_hat import SenseHat
import paho.mqtt.publish as publish
import requests
import time

# Instantiate a SenseHat() object
sense = SenseHat()

# Print a short message
print("Publishing data...")

# Send data in an infinite loop
x = 1
while True:
	tempC = sense.get_temperature()
	humidity = sense.get_humidity()
	pressure = sense.get_pressure()
	tempF = (tempC * 1.8) + 32
	psi = (pressure * 0.0145038)
#	data = [tempC, humidity, pressure, tempF, psi]
#	data = {'tempC':sense.get_temperature(), \
#	'humidity':sense.get_humidity()}

	# MQTT Messages
	msgs=[{'topic':"Capstone", 'payload':"The temperature is now"+" "\
		 + format(tempF, '.2f')+" degrees F"}]
	publish.multiple(msgs, hostname="192.168.99.6")
	time.sleep(2)

	# Push data to MongoDB as a "shadow copy"
#	test_data = {"Temperature": format(tempC, '.2f'), \
#		     "Pressure": format(psi, '.2f'), \
#		     "Humidity": format(humidity, '.2f')}
#	db.insert(test_data)
#	connection.close()


#########################
# Unused code (for now) #
#########################

#	      {'topic':"Capstone", 'payload':format(humidity, '.2f')},\
#	      {'topic':"Capstone", 'payload':format(pressure, '.2f')},\
#	      {'topic':"Capstone", 'payload':format(tempF, '.2f')},\
#	      {'topic':"Capstone", 'payload':format(psi, '.2f')}
#	     ]
#,hostname="192.168.99.115")

#	r = requests.put('http://52.90.52.137:3000/api/DKIOTmodels/', data={'Humidity':format(humidity, '.2f'), 'Pressure':format(pressure, '.2f'), 'Temperature':format(tempF, '.2f'), 'id':1})
#	print (r.text)
#	x += 1

#print("Welcome to DK IoT Weather Station! Our current conditions are: " \
#"Temperature: " + format(tempF, '.2f') + " degrees Farenheit " + \
#"Humidity: " + str(format(humidity, '.2f')) + "% rH " + \
#"Pressure: " + str(format(psi, '.2f')) + " psi")

# Ended up not using this code because of the infinite loop.  May want to
# incorporate later...
#print("Data sent!")
#time.sleep(1)
#print("Verifying the data...")
#r = requests.get('http://52.90.52.137:3000/api/DKIOTmodels/')

#x = 1
#while True:
#	print(r.text)
#	x += 1
