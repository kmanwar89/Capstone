#!/usr/bin/python

# This is a working file, but doesn't update the data autonomously

from sense_hat import SenseHat
import requests
import time

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

print("Sending data to DK IoT...")
r = requests.put('http://52.90.52.137:3000/api/DKIOTmodels/', \
data={'Humidity':format(humidity, '.2f'), 'Pressure':format(pressure, '.2f'), 'Temperature':format(tempF, '.2f'), 'id':1})
print("Data sent!")
time.sleep(1)
print("Verifying the data...")
r = requests.get('http://52.90.52.137:3000/api/DKIOTmodels/')
print(r.text)
