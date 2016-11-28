import requests

r = requests.put('http://rockmyglock.asuscomm.com:7000/api/tests', \
data={'temp':'10'})

print(r)
