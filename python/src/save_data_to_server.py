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


def save_data_val(pString, pJsondataasbytes):
    
        lServer = 'https://iot.porky.dev/ass3/app'
        req = urllib.request.Request(lServer + '/api/save/'+ pString)
        req.add_header('Content-Type', 'application/json; charset=utf-8')
        req.add_header('Content-Length', len(pJsondataasbytes))
        #print (jsondataasbytes)
        response = urllib.request.urlopen(req, pJsondataasbytes)
        
        txt_response = response.read()
        
        my_json = json.loads(txt_response)
        print(my_json)
        
def save_temp_humidity(pJson_databytes):
    time.sleep(10)
    save_data_val('temperature', pJson_databytes)
    time.sleep(10)
    save_data_val('humidity', pJson_databytes)
    time.sleep(10)
    
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
            ahk 
            temperature = json_data["temp"]
            time.sleep(1)

            humidity = json_data["humidity"]
            #motorPos = json_data["motorPos"]
            
            #save serial data to database
            save_req('temp', json_data)
            save_req('humidity', json_data)


if __name__ == '__main__':
    #save_temp_and_hum()
    save_test()
    #read_serial()
    #save_req('humidity')
    #save_req('temp')