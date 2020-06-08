import sys
sys.path.insert(1, './src')

from runFan import *
#from dc_motor import *
from servo_motor import ServoDevice

# this working_sample needs improvement
from working_sample import save_temp_and_hum
#####
from read_serial import read_serial
from json_data_processor import JsonDataProcessor
from get_config import PhysicalSystemConfiguration
from runFan import Fan

def set_actuator_parameters(pFan, pTemperature):
        #set actuator parameters(based on temperature values)
    fanOn = 0
    newMotorPos = 0
    if(sysConfig.extract_status() == "OFF"):
        #input values for both actuators based on temperature
        newMotorPos = servo_device.calculatePosFromTemp(pTemperature)
        fanIsOn = pFan.runFanwithTemperature(float(pTemperature))
    elif(sysConfig.extract_status() == "ON"):
        #input values for actuators from config file
        servoConfigPos = sysConfig.extract_motorPos()
        servo_device.move_servo(servoConfigPos)
        
        fanConfigIsOn = sysConfig.extract_fanIsOn()
        pFan.setFanSpeed(fanConfigIsOn)

        newMotorPos = 0
        fanIsOn = 100
        
    elif(sysConfig.extract_status() == "TEST"):
        #test but actuators to see if they are working. This should always work
        servo_device.test_range_of_motion()
        pFan.testFan()
        newMotorPos = 0
        fanOn = 100
        
        
    elif(sysConfig.extract_status() == "SWEEP"):
        #test only the servo. Fan runs based on temperature values
        servo_device.sweep_motor()
        fan.runFanwithTemperature(float(pTemperature))
        newMotorPos = 0
        fanOn = 100
    return newMotorPos, fanOn


def mainFunction():
    servo_device = ServoDevice()
    json_processor = JsonDataProcessor()
    sysConfig = PhysicalSystemConfiguration()
    fan = Fan()
    i = 0
    while True:
        print(i)
        # get online configuration of physical system
        sysConfig.get_config()
        
        serial_data = read_serial()
        json_data = json_processor.update_DataToProcess(serial_data)
        temperature = json_processor.get_temperature()
        
        #
        newMotorPos, fanOn = set_actuator_parameters(fan, temperature)

        #add actuator data to json
        json_processor.append_actuator_data_to_json(newMotorPos, fanOn)
        json_string = json_processor.get_json_string()
        print(json_string)
        i = i + 1

def mainSaveData():
    print("save data to database")    

if __name__ == '__main__':
    mainFunction()