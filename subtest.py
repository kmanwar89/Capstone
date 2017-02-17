#! /bin/python

# Script to test lots of subscription to a single topic
# Author: Kadar Anwar
# Date: 2-16-2017
# Python v3.4

import paho.mqtt.client as paho
 
def on_subscribe(client, userdata, mid, granted_qos):
    print("Subscribed: "+str(mid)+" "+str(granted_qos))
 
def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.qos)+" "+str(msg.payload))    
 
client = paho.Client()
client.on_subscribe = on_subscribe
client.on_message = on_message
client.connect(“192.168.99.75”, 1883)
client.subscribe(“Capstone/#”, qos=1)
 
client.loop_forever()
