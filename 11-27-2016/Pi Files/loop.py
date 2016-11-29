#!/usr/bin/python

# This is the same as the update.py file except w/ loops

from sense_hat import SenseHat
import requests
import time

sense = SenseHat()

#print("Welcome to DK IoT Weather Station! Our current conditions are: " \
#"Temperature: " + format(tempF, '.2f') + " degrees Farenheit " + \
#"Humidity: " + str(format(humidity, '.2f')) + "% rH " + \
#"Pressure: " + str(format(psi, '.2f')) + " psi")

print("Sending data to DK IoT...")

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

#print("Data sent!")
#time.sleep(1)
#print("Verifying the data...")
#r = requests.get('http://52.90.52.137:3000/api/DKIOTmodels/')

#x = 1
#while True:
#	print(r.text)
#	x += 1
