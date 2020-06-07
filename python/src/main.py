from writeToDB import *
from readSerialData import *
from runFan import *
#from dc_motor import *
from servo_motor import ServoDevice

if __name__ == "__main__":
    servo_device = ServoDevice()
    while(True):
        temp, isHot, motorPos = readSerialData()
        newMotorPos = servo_device.calculatePosFromTemp(temp)
        runFan(float(temp))
        writeToDB(temp, isHot, newMotorPos)
