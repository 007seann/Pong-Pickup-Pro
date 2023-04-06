import pygame
import time
from motors import Motors 
from time import time, sleep 
import cv2

#pygame.init()
#pygame.joystick.init()
#joystick = pygame.joystick.Joystick(0)

#joystick.init()
done = False

# Create an instance of the Motors class used in SDP 
mc = Motors() 
 
motor_id = 0
motor_id1 = 1 # The port that your motor is plugged in to
motor_id2 = 2
motor_id3 = 3
speed1 = -100
speed2 = 100# forward = positive, backwards = negative
speed3=60
run_time = 10        # number of seconds to run motors 
mc.move_motor(motor_id,50)
mc.move_motor(motor_id1,50)
mc.move_motor(motor_id2,50)
mc.move_motor(motor_id3,50)
sleep(10)
mc.stop_motor(motor_id)
mc.stop_motor(motor_id1)
mc.stop_motor(motor_id2)
mc.stop_motor(motor_id3)