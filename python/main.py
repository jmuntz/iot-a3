import sys
sys.path.insert(1, './src-luke')
sys.path.insert(2, './src')

from writeToDB import *
from readSerialData import *
from runFan import *
#from dc_motor import *
from servo_motor import ServoDevice

from working_sample import save_temp_and_hum
from read_serial import read_serial
from json_data_processor import JsonDataProcessor

import json



if __name__ == '__main__':
    servo_device = ServoDevice()
    json_processor = JsonDataProcessor()
    i = 0
    while True:
        print(i)
        serial_data = read_serial()
        json_data = json_processor.update_DataToProcess(serial_data)
        temperature = json_processor.get_temperature()
        
        #set actuator parameters(based on temperature values)
        newMotorPos = servo_device.calculatePosFromTemp(temperature)
        fanIsOn = runFan(float(temperature))
        
        #add actuator data to json
        json_processor.append_data_to_json(newMotorPos, fanIsOn)
        print(json_processor.get_json_string())
        i = i + 1

