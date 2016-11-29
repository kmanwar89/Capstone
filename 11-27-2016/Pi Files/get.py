#!/usr/bin/python

# Purpose: Small file to test GET requests from MongoDB via Loopback server hosted in an AWS
# T2 Micro instance.
# Author: Kadar M. Anwar
# Language: Python 3.5
# Date: 11-27-2016
# JMU ISAT Senior Capstone Project

# Import required libraries
import requests

# Print a message to the user
print("Verifying the data...")

# REST API get requests to a specific endpoint via our Loopback API
r = requests.get('http://52.90.52.137:3000/api/DKIOTmodels/583b40b8ddcc39004c348256')

# Print the resulting raw text
print(r.text)
