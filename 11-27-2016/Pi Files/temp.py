from sense_hat import SenseHat
import time

sense = SenseHat()

x = 1
while True:
	tempC = sense.get_temperature()
	tempF = (tempC * 1.8) + 32
	print("Temperature: " + format(tempF, '.2f') + " degrees Farenheit ")
	time.sleep(1)
	x += 1
