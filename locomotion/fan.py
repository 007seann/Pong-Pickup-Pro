
import socket
import sys
import time
from motors import Motors 
from time import time, sleep
import RPi.GPIO as GPIO

mc = Motors() 
 
motor_id = 0
motor_id1 = 1 # The port that your motor is plugged in to
motor_id2 = 2
motor_id3 = 3
motor_id4 = 4
straightSpeed = 50 # forward = positive, backwards = negative
k = 1
run_time = 10        # number of seconds to run motors



GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)


counter = 0


'''
while True:
    if count
    counter += 1
    print(counter)
    mc.move_motor(4,straightSpeed)#back right
    time.sleep(0.01)
''' 
    




mc.move_motor(0, 100)
#mc.move_motor(2, 10)
#mc.move_motor(3, 10)
# mc.move_motor(4,straightSpeed)#back right

sleep(10)
#mc.stop_motor(1)

# mc.move_motor(4,straightSpeed)#back right

#mc.stop_motor(2)

mc.stop_motor(0)
