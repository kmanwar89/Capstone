#!/usr/bin/python

# Purpose: Gather Temp, Humidity & Pressure data from SenseHAT
# sensor device and send to MongoDB via Loopback API
# Author: Kadar M. Anwar
# Language: Python 3.5
# Date: 11-27-2016
# JMU ISAT Senior Capstone Project

# v1.0 - used update.py file as base, this file includes a loop to allow for
# autonomous updates w/o user interaction.

# Import required libraries
from sense_hat import SenseHat
import requests
import time

# Instantiate a SenseHat() object
sense = SenseHat()

#print("Welcome to DK IoT Weather Station! Our current conditions are: " \
#"Temperature: " + format(tempF, '.2f') + " degrees Farenheit " + \
#"Humidity: " + str(format(humidity, '.2f')) + "% rH " + \
#"Pressure: " + str(format(psi, '.2f')) + " psi")

# Print a short message
print("Sending data to DK IoT...")

# Send data in an infinite loop
x = 1
while True:
	tempC = sense.get_temperature()
	humidity = sense.get_humidity()
	pressure = sense.get_pressure()
	tempF = (tempC * 1.8) + 32
	psi = (pressure * 0.0145038)

	r = requests.put('http://52.90.52.137:3000/api/DKIOTmodels/', data={'Humidity':format(humidity, '.2f'), 'Pressure':format(pressure, '.2f'), 'Temperature':format(tempF, '.2f'), 'id':1})
	print (r.text)
	x += 1

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
