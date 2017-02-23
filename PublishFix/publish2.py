import paho.mqtt.client as paho
import time
 
def on_publish(client, userdata, mid):
    print("mid: "+str(mid))
 
client = paho.Client()
client.on_publish = on_publish
client.connect("192.168.99.75", 1884)
client.loop_start()
topic = "Capstone"
 
while True:
	temperature = 95.72
	(rc, mid) = client.publish(topic, str(temperature), qos=1, retain=True)
#    time.sleep(30)
    #temperature = read_from_imaginary_thermometer()
