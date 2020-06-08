from dc_motor import *
    

def runFan(pTemp):
    if (pTemp > 20):
        motorON()
        return True
    elif (pTemp < 20):
        motorOFF()
        return False
    else:
        motorOFF()
        return False



if __name__ == "__main__":
    while(True):
#        runFan(20)
        #motorOFF()
        my_pwm.start(0)
        time.sleep(1)
        my_pwm.start(96)
        time.sleep(1)