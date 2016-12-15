#!/usr/bin/python
# This file provides a demonstration of sending a GET request from the client
# to the web-hosted MongoDB to retrive a data point or set of data points.

import requests

print("Verifying the data...")
x = 1
while True:
	r = requests.get('http://54.237.212.2:3000/api/DKIOTmodels/')
	print(r.text)
