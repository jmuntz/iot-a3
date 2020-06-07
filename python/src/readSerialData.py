import serial
#from dc_motor import *

device = '/dev/ttyACM0'
arduino = serial.Serial(device, 9600)

#dataTemp = arduino.readline()
def readSerialData(): 
    temp = 5
    motorPos = 50
    hIndex = 4
    isHot = False

    i = 0
    while(i<3):
        dataIndicator = arduino.readline()
        indicator = dataIndicator.decode().strip()
        ind = indicator
        print("ind: " + ind)
        #print(dataIndicator)
        if(ind == 'temp'):
    #         print('test 1st if in while loop')
            dataTemp = arduino.readline()
            temp = dataTemp.decode('UTF-8')
            tempInt = temp.strip()
            i = i + 1
        elif(indicator == "index"):
            dataHeatIndex = arduino.readline()
            hIndex = dataHeatIndex.decode('UTF-8')
            i = i + 1
        elif(indicator == "pos"):
            dataMotorPos = arduino.readline()
            motorPos = dataMotorPos.decode('UTF-8')
            i = i + 1

    print('Encoded Serial Temp: ' + str(temp))
    print('Encoded Serial Heat Index: '+ hIndex)
    print('Encoded Serial Motor Position: '+ motorPos)

    
    isHot = checkTemp(temp, isHot)
    return temp, isHot, motorPos

    
#################################

def checkTemp(pTemp, pIsHot):
    if(float(pTemp)>20):
        pIsHot = True
        #motorON()
    elif(float(pTemp)<20):
        pIsHot = False
       # motorOFF()    
    return pIsHot    
