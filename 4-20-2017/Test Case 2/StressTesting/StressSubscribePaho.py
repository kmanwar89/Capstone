#! /bin/python

# Script to test lots of subscription to a single topic
# Author: Kadar Anwar
# Date: 2-16-2017
# Python v3.4

# v0.1 - initial code
# v0.2 - 2/23/2017 - updated code for a simple loop with lots of subscriptions
# 	to a single topic

import paho.mqtt.client as paho
import time

client.username_pw_set(admin, password=admin)

client = paho.Client()
client.connect("192.168.99.75", 1883)

print("Beginning subscription stress test...")

z = 0
for x in range(0,1000):
    for y in range(0,100):
        client.subscribe("Capstone")
        z+=1

print("Sent", x*y, "packets out of", z, "total packets")
#print("Subscribed to topic", x*y, "times")

#client.loop_forever()
