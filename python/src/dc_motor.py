import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
PIN = 2
GPIO.setup(PIN, GPIO.OUT)
my_pwm = GPIO.PWM(PIN, 100)


my_pwm.start(0)

def motorON():
    my_pwm.start(97)
        
def motorOFF():
    my_pwm.start(0)
    
if __name__ == "__main__":
    while(True):
#        runFan(20)
        #motorOF`F()
        print("turn OFF")
        my_pwm.start(0)
        time.sleep(1)
        print("turn ON")
        my_pwm.start(96)
        time.sleep(1)

