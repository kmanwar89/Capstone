#! /bin/bash

# Purpose: Publish messages to an MQTT broker through an infinite loop
# in order to stress test the MQTT broker and other components of the IoT
# Architecture.

# Author: Kadar M. Anwar
# Language: bash
# Dependency: mosquitto-clients
# ISAT Senior Capstone Project

# v0.1 - 2/22/2017 - Initial code
# v0.2 - 4/9/2017 - Updated code and description

while :
do
	mosquitto_pub -h 192.168.1.218 -t Capstone -m "Blah" -p 1883
done
