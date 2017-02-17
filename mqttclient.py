#! /bin/python

# Author: Kadar Anwar
# Date: 2-16-2017
# Python v3.4

import paho.mqtt.client as paho

def on_connect(client, userdata, flags, rc):
        print("CONNACK received with code %d." % (rc))

client = paho.Client()
client.on_connect = on_connect
client.connect("192.168.99.75", 1883)
