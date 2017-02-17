#! /bin/python

# Script to subscribe to lots of topics
# Author: Kadar Anwar
# Date: 2-16-2017
# Python v3.4

import paho.mqtt.client as paho
import time

def on_publish(client, userdata, mid):
	print("mid: "+str(mid))

client = paho.Client()
client.on_publish = on_publish
client.connect("192.168.99.75", 1883)
client.loop_start()

while True:
	temperature = 
	
