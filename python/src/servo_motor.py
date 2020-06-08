from gpiozero import Servo
from numpy import arange
import time



class ServoDevice:
    servo_pin = 17
    
    def __init__(self, servo_position=0):      
        self.servo = Servo(self.servo_pin)
       # self.move_servo(servo_position)
    
    def validator(self, pPos):
        #print("run validator")
        if(pPos < -1):
            print("Value is below minimum range for servo!")
            print(pPos)
            pPos = -1
#            return pPos
        elif(pPos > 1):
            print("Value is above maximum range for servo!")
            print(pPos)
            pPos = 1
        
        return pPos


    def move_servo(self, servo_position):
        #self.servo.value=self.convert_percentage_to_integer(servo_position)
        servo_position = self.validator(servo_position)
        self.servo.value=servo_position

    def convert_percentage_to_integer(self, percentage_amount):
        return (percentage_amount*0.02)-1
    

    def calculatePosFromTemp(self, data):
        maxPos = -1 #value is in degrees
        minPos = 1
        totalRange = abs(maxPos) + abs(minPos)
        maxTemp = 50 # value is in Celcius
        conversionVal = totalRange/maxTemp
        currentTemp = data
        nextPos = 0
        if(float(currentTemp) > 25):
            nextPos = minPos
        elif(float(currentTemp) < 18.5):
            nextPos = maxPos
        else:
            nextPos = float(currentTemp) * conversionVal
       
        print(nextPos)
        self.move_servo(nextPos)
        time.sleep(1)
        self.servo.detach()
        return nextPos
    
    def sweep_motor(self):
        pos = 0  
        speedRateLimiter = .02
        #(pos = 0 pos <= 171 pos += 1)
        for x in arange(-1, 1, 0.05):
            pos = x
            self.move_servo(pos)
            time.sleep(speedRateLimiter)
        #(pos = 172 pos >= 0 pos -= 1)  
        for x in arange(1, -1, -0.05):
            pos = x
            self.move_servo(pos)
            time.sleep(speedRateLimiter)
            
    def test_range_of_motion(self):
        servo_device.sweep_motor()
        servo_device.servo.max()
        time.sleep(1)
        servo_device.servo.mid()
        time.sleep(1)
        servo_device.servo.min()
        time.sleep(1)
        servo_device.servo.detach()
        
    def test_calculation(self, data):
        newPos = servo_device.calculatePosFromTemp(data)
        servo_device.move_servo(newPos)
        time.sleep(1)
        servo_device.servo.detach()
        
if __name__=="__main__":
    servo_device = ServoDevice(80)
    servo_device.test_range_of_motion()
    #servo_device.test_calculation(20)
    #while(True):

    #while(True):
     #   servo_device.sweep_motor()
     #   print("test")