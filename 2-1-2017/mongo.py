#!/usr/bin/python

# Purpose: Gather Temp, Humidity & Pressure data from SenseHAT
# sensor device, publish over an MQTT topic and send a shadow copy
# to MongoDB for redundancy purposes.

# Author: Kadar M. Anwar
# Language: Python 3.5
# Date: 11-27-2016
# JMU ISAT Senior Capstone Project

# v1.0 11/27/2016 - used update.py file as base, this file includes a loop to
# allow for autonomous updates w/o user interaction.

# v1.1 1/22/2017 - updated to incorporate MQTT publish messages rather than
# API and HTTP-based messages

# v1.2 1/30/2017 - updated to incorporate publishing MQTT messages to MongoDB 
# as a form of "shadow copy" capability

# v1.2a 1/30/2017 - cleaned up code a little bit, added unused code to the
# bottom of the file.

# Import required libraries
from sense_hat import SenseHat
import paho.mqtt.publish as publish
import requests
import time
from pymongo import MongoClient

# MongoDB stuff
connection = MongoClient(host='192.168.99.180',port=27017)

db = connection.DKFinal.pistats

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
		 + format(tempC, '.2f')+" degrees F"}]
	publish.multiple(msgs, hostname="192.168.99.73")
	time.sleep(3)

	# Push data to MongoDB as a "shadow copy"
	test_data = {"Temperature": format(tempC, '.2f'), \
		     "Pressure": format(psi, '.2f'), \
		     "Humidity": format(humidity, '.2f')}
	db.insert(test_data)
	connection.close()



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
