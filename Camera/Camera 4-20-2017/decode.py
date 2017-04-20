import paho.mqtt.client as mqtt
import base64

def on_connect(client, userdata, rc):
    print("Connect with result code " + str(rc))
    client.subscribe("MyHome")

def on_message(client, userdata, msg):
    #print("Topic : " , msg.topic + "\n Image : " + msg.payload)


    text = open('test.txt','w')
    fileContent=text.read()
    text.close()
    decoded = base64.b64decode(fileContent)

    picture = open('/home/kadar/Desktop/test.jpg','w')
    picture.write(str(decoded))
    picture.close()

    print('Image written')


    # f.write(str(msg.payload))
    # f2.write(str(msg.payload))
    # f2.close()
    # f.close()
    # print("Image output to Desktop")


# Instantiate the client object, connect to broker &
# loop forever
client = mqtt.Client()
client.connect("192.168.99.75", 1883, 60)
client.on_connect = on_connect
client.on_message = on_message
client.loop_forever()
