import requests
import json

baseUrl = 'https://api.upcitemdb.com/prod/trial/lookup'
param = {'upc' : '012993441012'}
response = requests.get(baseUrl, params=param)

content = response.content
info = json.loads(content)
print(info['items'][0]['title'])