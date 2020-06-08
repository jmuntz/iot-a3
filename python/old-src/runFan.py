from dc_motor import *
    
class Fan:

    def runFanwithTemperature(self, pTemp):
        if (pTemp > 20):
            motorON()
            return True
        elif (pTemp < 20):
            motorOFF()
            return False
        else:
            motorOFF()
            return False


    def setFanSpeed(self, speed):
        if(speed <= 10):
            speed = 0
            print("Fan needs more power!!!")
        if(speed < 30 and speed > 10):
            speed = 30
        elif(speed > 98):
            speed = 98
        my_pwm.start(speed)

    def fanOff(self):
        my_pwm.start(0)

    def fanOn(self):
        my_pwm.start(96)
        
    def testFanOnOff(self):
        self.fanOn()
        time.sleep(1)
        self.fanOff()
        time.sleep(1)
        self.fanOn()
        time.sleep(1)
        self.fanOff()
        time.sleep(1)
        
    def testFanSpeed(self):
        for i in range(29, 101):
            print(i)
            my_pwm.start(i)
            time.sleep(0.1)
            if(i == 100):
                break
        time.sleep(4)
        self.fanOff()
        
    def testFan(self):
        self.testFanOnOff()
        self.testFanSpeed()

if __name__ == "__main__":
    fan = Fan()
    while(True):
#        runFan(20)
        #motorOFF()
        #testFan()
        fan.testFan()
        break
        #my_pwm.start(110)
