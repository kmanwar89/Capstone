import base64
import paho.mqtt.client as mqtt

topic = input("What is the topic to send the encoded image to?: ")
host = "192.168.99.75"

# Instantiate objects
client = mqtt.Client()

# Connect to the broker over MQTT port
client.username_pw_set("admin","admin")
client.connect(host, port=1883, keepalive=60)

# Picture Processing

with open("abc.jpg", "rb") as imageFile: # Open a file handler
    fileContent = imageFile.read()  # Read the file
    byteArr=bytes(fileContent)  # Convert to bytes
    str = base64.b64encode(byteArr) # Pass the bytes to base64 to encode

#    str = base64.b64encode(imageFile.read())
#    str = str[1:len(str)-1]

# Publish a message to the "MyHome" topic
print(str)
client.publish(topic, str, qos=0)
print('')
print('')
print('Message published to the "' + topic + '" topic')

# Keep the connection open
client.loop_start()
