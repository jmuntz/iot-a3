import serial
from serial import Serial
import socket
import sys
import json
import time



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
            
if __name__ == '__main__':
    read_serial()
