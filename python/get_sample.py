import requests, json
import urllib.request, urllib.parse
from urllib import request, parse
import random

url = "http://iot.porky.dev/ass3/app/api/get/temperature/5"

randnum = random.randint(10,26)

contents = urllib.request.urlopen(url).read()

r = requests.get(url)
req = urllib.request.Request(url)
parsed = urllib.request.urlopen(req).read()
cont = json.loads(parsed.decode('utf-8'))
