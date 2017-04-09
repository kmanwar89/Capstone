# Import libraries
import paho.mqtt.client as mqtt
import time

# Define variables
host = ''

# Instantiate objects
client = mqtt.Client()

# Get the IP address from the user
host = input('Please enter the IP address of the broker you wish to test: ')

# Connect to the broker over MQTT port
client.connect(host, port=1883, keepalive=60)
client.loop_start() # Keep the connection open

# Loop of 1 million publish packets, published to the "Capstone" topic
z = 0
for x in range(1,10001):
	for y in range (1,10001):
		client.publish("Capstone", payload = "Stress test", qos=0)
		z+=1
		#print(z, "packets sent")

print("Packets sent successfully: ", x*y)
print("Total packets sent: ", z)
