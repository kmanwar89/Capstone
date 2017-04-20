import paho.mqtt.client as mqtt

host = "192.168.99.75"

def on_connect(client, userdata, rc):
    print("Connect with result code " + str(rc))
    client.subscribe(“MyHome”)

def on_message(client, userdata, msg):
    #print("Topic : " , msg.topic + "\n Image : " + msg.payload
    f = open('/home/kadar/Desktop/test.jpg', 'w')
    f.write(msg.payload)
    f.close()
    print('Image written to /home/kadar/Desktop/test.jpg')

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect(host, 1883, 60)
client.loop_forever()
