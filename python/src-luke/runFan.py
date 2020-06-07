from dc_motor import *
    

def runFan(pTemp):
    if (pTemp > 20):
        motorON()
    elif (pTemp < 20):
        motorOFF()
    else:
        motorOFF()            



if __name__ == "__main__":
    while(True):
#        runFan(20)
        #motorOFF()
        my_pwm.start(0)
        time.sleep(1)
        my_pwm.start(96)
        time.sleep(1)