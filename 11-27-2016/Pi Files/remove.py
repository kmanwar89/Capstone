#!/usr/bin/python

# Purpose: Small file to test how data can be removed from database via Loopback API
# Author: Kadar M. Anwar
# Language: Python 3.5
# Date: 11-27-2016
# JMU ISAT Senior Capstone Project

# Import required libraries
import requests

# Print a short message
print("Deleting data...")

# Delete a specific endpoint in our MongoDB via the Loopback API
r = requests.delete('http://52.90.52.137:3000/api/DKIOTmodels/583b40b8ddcc39004c348256')

# Print the resulting output text; an error message proves the endpoint was successfully deleted.
print(rget)
