#! /bin/bash

while :
do
	mosquitto_pub -h 172.17.0.132 -t Capstone -m "Blah" -p 1883
done
