#!/usr/bin/python

import requests

print("Verifying the data...")
r = requests.get('http://52.90.52.137:3000/api/DKIOTmodels/583b40b8ddcc39004c348256')
print(r.text)
