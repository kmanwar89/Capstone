#! /bin/bash

# Purpose: Publish messages to an MQTT broker through an infinite loop
# in order to stress test the MQTT broker and other components of the IoT
# Architecture.

# Author: Kadar M. Anwar
# Language: bash
# Date: 2-22-2017
# JMU ISAT Senior Capstone Project

while :
do
	mosquitto_pub -h 192.168.1.218 -t Capstone -m "Blah" -p 1883
done
