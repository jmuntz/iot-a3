import urllib.request
import json
import random

randnum = random.randint(10,26)

body = {'id':'133','host':'111.111.111.222','timestamp':'1590824976','data':randnum}

myurl = "http://iot.porky.dev/ass3/app/api/save/dump"

req = urllib.request.Request(myurl)
req.add_header('Content-Type', 'application/json; charset=utf-8')
jsondata = json.dumps(body)
jsondataasbytes = jsondata.encode('utf-8')   # needs to be bytes
req.add_header('Content-Length', len(jsondataasbytes))
print (jsondataasbytes)
response = urllib.request.urlopen(req, jsondataasbytes)

my_json = json.loads(response.read())
