import base64
import paho.mqtt.client as mqtt
import time

image = input("Enter the filename of the image you would like to send: ")

f = open(image, "rb")
data = f.read()
f.close()

encoded = base64.b64encode(data)

print("Image has been encoded as base64")
time.sleep(2)

topic = input("What is the topic to send the encoded image to?: ")
host = input("Enter the IP address of the MQTT broker: ")

# Instantiate objects
client = mqtt.Client()

# Connect to the broker over MQTT port
#client.username_pw_set("admin","admin")
client.connect(host, port=1883, keepalive=60)

print("Publishing picture to", topic)
client.publish(topic, encoded, qos=0)
print('')
print('')
print('Message published to the "' + topic + '" topic')

# Keep the connection open
client.loop_start()

# with open("abc.jpg", "rb") as imageFile: # Open a file handler
#     fileContent = imageFile.read()  # Read the file
#     byteArr=bytes(fileContent)  # Convert to bytes
#     str = base64.b64encode(byteArr) # Pass the bytes to base64 to encode

#    str = base64.b64encode(imageFile.read())
#    str = str[1:len(str)-1]

# Publish a message to the "MyHome" topic
#print(str)


# Original code from 4/13/2017
# # Import libraries
# import paho.mqtt.client as mqtt
# import time
# import base64
#
# # Instantiate objects
# client = mqtt.Client()
#
# # Connect to the broker over MQTT port
# client.connect("192.168.99.75", port=1883, keepalive=60)
#
# # Picture Processing
# f=open("abc.jpg","rb") # file is in the same directory, relative path
# fileContent=f.read()
# byteArr = base64.b64encode(fileContent)
#
# # Publish a message to the "Capstone" topic
# client.publish("MyHome", byteArr, qos=0)
#
#  # Keep the connection open
# client.loop_start()
