import urllib.request
from urllib.error import HTTPError
import json
import random


def save_sample():
    randnum = random.randint(10,26)

    body = {'id':'10','host':'192.168.0.13','timestamp':'1590821980','data':randnum}

    myurl = "http://iot.porky.dev/ass3/app/api/save/temperature"

    req = urllib.request.Request(myurl)
    try:
        handler = urllib.request.urlopen(req)
    except HTTPError as e:
        content = e.read()
        print(content)
    req.add_header('Content-Type', 'application/json; charset=utf-8')
    jsondata = json.dumps(body)
    jsondataasbytes = jsondata.encode('utf-8')   # needs to be bytes
    req.add_header('Content-Length', len(jsondataasbytes))
    print (jsondataasbytes)
    response = urllib.request.urlopen(req, jsondataasbytes)

    my_json = json.loads(response.read())


if __name__=="__main__":
    save_sample()