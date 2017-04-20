# Import libraries
import paho.mqtt.client as mqtt
import time
import base64

# Instantiate objects
client = mqtt.Client()

# Connect to the broker over MQTT port
client.connect("192.168.99.75", port=1883, keepalive=60)

# Picture Processing
f=open("abc.jpg","rb") # file is in the same directory, relative path
fileContent=f.read()
byteArr = base64.b64encode(fileContent)

# Publish a message to the "Capstone" topic
client.publish("MyHome", byteArr, qos=0)

 # Keep the connection open
client.loop_start()
