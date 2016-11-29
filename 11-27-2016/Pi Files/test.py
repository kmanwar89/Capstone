from sense_hat import SenseHat
import time

sense = SenseHat()

x = 1
while True:
	gyro_only = sense.get_gyroscope()
	print("p: {pitch}, r: {roll}, y: {yaw}".format(**gyro_only))
	time.sleep(1)
	x += 1
