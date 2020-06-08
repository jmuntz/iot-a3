import sys
sys.path.insert(1, './src-luke')
from writeToDB import *
from readSerialData import *
from runFan import *
#from dc_motor import *
from servo_motor import ServoDevice

from working_sample import save_temp_and_hum