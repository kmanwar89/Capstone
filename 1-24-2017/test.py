#! /usr/bin/python

import paho.mqtt.publish as publish
publish.single ("mqtt", payload="test", hostname="192.168.99.73")
