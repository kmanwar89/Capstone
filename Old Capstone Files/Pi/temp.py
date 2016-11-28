#!/usr/bin/python

from sense_hat import SenseHat
import requests

sense = SenseHat()

tempC = sense.get_temperature()
humidity = sense.get_humidity()
pressure = sense.get_pressure()

tempF = (tempC * 1.8) + 32
psi = (pressure * 0.0145038)
print("Welcome to DK IoT Weather Station! Our current conditions are: " \
"Temperature: " + format(tempF, '.2f') + " degrees Farenheit " + \
"Humidity: " + str(format(humidity, '.2f')) + "% rH " + \
"Pressure: " + str(format(psi, '.2f')) + " psi")

r = requests.put('http://52.90.52.137:3000/api/DKIOTmodels/', \
	data={'Humidity':humidity, 'Pressure':pressure, 'Temperature':tempF})

