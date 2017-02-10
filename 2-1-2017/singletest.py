#! /usr/bin/python

# Test file to figure out how to send data from Python into a MongoDB

# 1-30-2017

# v1.0
from pymongo import MongoClient

connection = MongoClient(host='192.168.99.75',port=27017)

db = connection.test.testcollection

test_data = {"name" : "vicki", "age" : "21", "major" : "isat"}

db.insert(test_data)

#db.insert({"name" : "Devon", "age" : "27", "major" : "isat"})

connection.close()
