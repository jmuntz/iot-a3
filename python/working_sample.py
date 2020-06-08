import serial
from serial import Serial
import socket
import sys
import json
import time
import requests

import urllib.request
import random

randnum = random.randint(10,26)

server = 'https://iot.porky.dev/ass3/app'

# posty = requests.post(host + '/functions.php', params=test_data, headers = {"User-Agent": "Firefox/12.0"});


def save_req(pString):
    print(pString)
    req = urllib.request.Request(server + '/api/save/' + pString)
    req.add_header('Content-Type', 'application/json; charset=utf-8')

    req.add_header('Content-Length', len(jsondataasbytes))
    #print (jsondataasbytes)
    response = urllib.request.urlopen(req, jsondataasbytes)
    
    txt_response = response.read()
    
    my_json = json.loads(txt_response)   
    print(my_json)


def read_serial():
    ser = serial.Serial('/dev/ttyACM0', 115200, timeout=1)
    ser.flush()
    ser.reset_input_buffer()
    ser.reset_output_buffer()
    while True:
        if ser.in_waiting > 0:
            data = ser.readline().decode('utf-8').rstrip(' ')
            print("SERIAL DATA: " + "["+data+"]")
            json_data = json.loads(data)
            
            temperature = json_data["temp"]
            humidity = json_data["humidity"]
            #motorPos = json_data["motorPos"]

def save_temp_and_hum():
    
    ser = serial.Serial('/dev/ttyACM0', 115200, timeout=1)
    ser.flush()
    ser.reset_input_buffer()
    ser.reset_output_buffer()
    
    while True:
        if ser.in_waiting > 0:
            data = ser.readline().decode('utf-8').rstrip(' ')
            print("SERIAL DATA: " + "["+data+"]")
            json_data = json.loads(data)
            
            temperature = json_data["temp"]
            humidity = json_data["humidity"]
            
            
            #if is_json(data):
           
            temp_req = urllib.request.Request(server + '/api/save/temperature')
            temp_req.add_header('Content-Type', 'application/json; charset=utf-8')
            jsondata = json.dumps(json_data)
            jsondataasbytes = jsondata.encode('utf-8')   # needs to be bytes
            temp_req.add_header('Content-Length', len(jsondataasbytes))
            #print (jsondataasbytes)
            temp_response = urllib.request.urlopen(temp_req, jsondataasbytes)
            
            txt_response = temp_response.read()
            
            my_json = json.loads(txt_response)   
            print(my_json)
            
            hum_req = urllib.request.Request(server + '/api/save/humidity')
            hum_req.add_header('Content-Type', 'application/json; charset=utf-8')

            hum_req.add_header('Content-Length', len(jsondataasbytes))
            #print (jsondataasbytes)
            hum_response = urllib.request.urlopen(hum_req, jsondataasbytes)
            
            txt_response = hum_response.read()
            
            my_json = json.loads(txt_response)   
            print(my_json)
        #ser.flush()

if __name__ == '__main__':
    #save_temp_and_hum()
    read_serial()
    save_req('humidity')
    save_req('temp')