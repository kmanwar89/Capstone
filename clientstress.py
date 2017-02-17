#! /bin/python
import paho.mqtt.publish as publish

#publish.connect(192.168.99.75, port=1884, keepalive=60,  bind_address="")

#publish.subscribe(Capstone)

#publish.single(Capstone, payload="Test", hostname="192.168.99.75", \
#	port=1884, client_id="stress")

x = 1
while True:
	msgs=[{'topic':"Capstone", 'payload':"Stress test string"}]
	publish.multiple(msgs, hostname="192.168.99.75")
#	time.sleep(2)
