import paho.mqtt.client as mqtt
import base64

topic = input("What is the topic to subscribe to?: ")
host = "192.168.99.75"

def on_connect(client, userdata, rc):
    print("Connect with result code " + str(rc))
    client.subscribe(topic)

def on_message(client, userdata, msg):
    #print("Topic : " , msg.topic + "\n Image : " + msg.payload)
    f = open('/home/kadar/Desktop/output.jpg', 'w') # Open an image to write to
    decoded = base64.b64decode(msg.payload)    # Decode the payload
    f.write(str(decoded))   # Write the decoded bytes
    f.close()   # Close the file handler

    print('Image written')   # Inform the user

    # text = open('test.txt','w')
    # fileContent=text.read()
    # text.close()
    # decoded = base64.b64decode(fileContent)
    #
    # picture = open('/home/kadar/Desktop/test.jpg','w')
    # picture.write(str(decoded))
    # picture.close()



    # f.write(str(msg.payload))
    # f2.write(str(msg.payload))
    # f2.close()
    # f.close()
    # print("Image output to Desktop")


# Instantiate the client object, connect to broker &
# loop forever
client = mqtt.Client()
client.username_pw_set("admin","admin")
client.connect("192.168.99.75", 1883, 60)
client.on_connect = on_connect
client.on_message = on_message
client.loop_forever()



#
#
#
#
# import paho.mqtt.client as mqtt
#
#
# def on_connect(client, userdata, rc):
#     print("Connect with result code " + str(rc))
#     client.subscribe(“MyHome”)
#
# def on_message(client, userdata, msg):
#     #print("Topic : " , msg.topic + "\n Image : " + msg.payload
#     f = open('/home/kadar/Desktop/test.jpg', 'w')
#     f.write(msg.payload)
#     f.close()
#     print('Image written to /home/kadar/Desktop/test.jpg')
#
# client = mqtt.Client()
# client.on_connect = on_connect
# client.on_message = on_message
# client.connect(host, 1883, 60)
# client.loop_forever()
