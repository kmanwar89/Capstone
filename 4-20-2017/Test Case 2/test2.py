import os

for x in range(1,1001):
	for y in range(1,1001):
		os.system('mosquitto_pub -h 192.168.98.75 -p 1883 -t "MyHome" -u admin -P admin -m "TEST2"')

