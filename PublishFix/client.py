#!/usr/bin/python

# Python MQTT Client

# Purpose: This file is an MQTT client implementation using the Paho
# MQTT Python library. Offers same functionality as mosquitto_sub.

# Author: Kadar M. Anwar
# Language: Python 3.5
# Date: 2-22-2017
# JMU ISAT Senior Capstone Project

import paho.mqtt.client as mqtt

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, rc):
    print("Connected with result code "+str(rc))
    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    #client.subscribe("$SYS/#")
    client.subscribe("Capstone")

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
	print(msg.topic+" "+str(msg.payload))

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("192.168.1.218", 1883, 15)

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
client.loop_forever()
