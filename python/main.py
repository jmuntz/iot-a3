import sys
sys.path.insert(1, './src-luke')
from writeToDB import *
from readSerialData import *
from runFan import *
#from dc_motor import *
from servo_motor import ServoDevice

from working_sample import save_temp_and_hum

def append_data_to_json(pJson_data):
    
    x = {"fanOn": False}
    # python object to be appended 
    y = {"motorPos":110096} 
      
    # parsing JSON string: 
    z = json.loads(pJson_data) 
       
    # appending the data 
    z.update(y)
    z.update(x) 
    # the result is a JSON string: 
    print(json.dumps(z))
    return z

if __name__ == '__main__':
    while True:
        json_data = read_serial()
        new_json_data = append_data_to_json(json_data)
        temp = new_json_data["temperature"]
        newMotorPos = servo_device.calculatePosFromTemp(temp)
        runFan(float(temp))

