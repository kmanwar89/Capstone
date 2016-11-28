import requests

#payload = {'key1': 'value1', 'key2': 'value2'}
#r = requests.post('https://api.github.com/events')

r = requests.get('http://192.168.99.108:3000/api/Capstones')

#r = requests.put('http://192.168.1.222:3000/api/SmartClickrs', \
#	data={'name':'Test2', 'city':'city2', 'id':'2'})

print(r.text)
