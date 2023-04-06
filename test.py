import pygame
import time
from motors import Motors 
from time import time, sleep 
import cv2
import RPi.GPIO as GPIO
'''
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

TRIG = 24
ECHO = 23

GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)

def Distance_Ultrasound():
    GPIO.output(TRIG,GPIO.LOW)
    sleep(0.000002)
    GPIO.output(TRIG,GPIO.HIGH)
    sleep(0.00001)
    GPIO.output(TRIG,GPIO.LOW)
    while GPIO.input(ECHO) ==0:
        emitTime = time()
    while GPIO.input(ECHO)==1:
        acceptTime = time()
    totalTime = acceptTime - emitTime
    distanceReturn = totalTime * 340 /2 * 100
    return distanceReturn

count = 0
while True:
    print(Distance_Ultrasound())
    sleep(1)
    count=count+1
    if (count == 10):
        break

'''
pygame.init()
pygame.joystick.init()
joystick = pygame.joystick.Joystick(0)

joystick.init()
done = False

# Create an instance of the Motors class used in SDP 
mc = Motors() 
 
motor_id = 0
motor_id1 = 1 # The port that your motor is plugged in to
motor_id2 = 2
motor_id3 = 3
motor_id4 = 4
speed1 = -100
speed2 = 100# forward = positive, backwards = negative
speed3=60
run_time = 10        # number of seconds to run motors 


#vid = cv2.VideoCapture(0)
#fourcc = cv2.VideoWriter_fourcc(*'XVID')
#video_writer = cv2.VideoWriter("video.avi", fourcc, 30, (640,480))

#while not done:
    #ret, frame = vid.read()
    #video_writer.write(frame)
    #print("recording")
    #if cv2.waitKey(1) and joystick.get_button(6)==1 and joystick.get_button(7)==1:
    #    done=True
'''
while not done:
    for event_ in pygame.event.get():
        
        if event_.type == pygame.JOYBUTTONDOWN:
            if joystick.get_button(0)==1 and joystick.get_button(1)==1:
                print('BA')
                mc.move_motor(motor_id,50)#back left
                mc.move_motor(motor_id1,0)#back right
                mc.move_motor(motor_id2,0)#front left
                mc.move_motor(motor_id3,50)#front right
            elif joystick.get_button(3)==1 and joystick.get_button(0)==1:
                print('XA')
                mc.move_motor(motor_id,0)#back left
                mc.move_motor(motor_id1,50)#back right
                mc.move_motor(motor_id2,50)#front left
                mc.move_motor(motor_id3,0)#front right
            elif joystick.get_button(4)==1 and joystick.get_button(3)==1:
                print('XY')
                mc.move_motor(motor_id,0)#back left
                mc.move_motor(motor_id1,-50)#back right
                mc.move_motor(motor_id2,-50)#front left
                mc.move_motor(motor_id3,0)#front right
            elif joystick.get_button(4)==1 and joystick.get_button(1)==1:
                print('YB')
                mc.move_motor(motor_id,-50)#back left
                mc.move_motor(motor_id1,0)#back right
                mc.move_motor(motor_id2,0)#front left
                mc.move_motor(motor_id3,-50)#front right
            elif joystick.get_button(1)==1:
                print('B')#B
                mc.move_motor(motor_id,speed1)#back right
                mc.move_motor(motor_id1,speed2)#back left
                mc.move_motor(motor_id2,speed1)#front right
                mc.move_motor(motor_id3,speed2)#front left
            elif joystick.get_button(4)==1:
                print('Y')#Y
                mc.move_motor(motor_id,speed1)#back left
                mc.move_motor(motor_id1,speed1)#back right
                mc.move_motor(motor_id2,speed1)#front left
                mc.move_motor(motor_id3,speed1)#front right
            elif joystick.get_button(3)==1:
                print('X')#X
                mc.move_motor(motor_id,speed2)#back left
                mc.move_motor(motor_id1,speed1)#back right
                mc.move_motor(motor_id2,speed2)#front left
                mc.move_motor(motor_id3,speed1)#front right
            elif joystick.get_button(0)==1:
                print('A')#A
                mc.move_motor(motor_id,speed2)#back left
                mc.move_motor(motor_id1,speed2)#back right
                mc.move_motor(motor_id2,speed2)#front left
                mc.move_motor(motor_id3,speed2)#front right
            elif joystick.get_button(6)==1:
                print("LB")
                if (speed1!=0):
                    speed1+=10
                    speed2-=10
                print(speed1)
                print(speed2)
            elif joystick.get_button(7)==1:
                print("RB")
                if (speed2!=100):
                    speed1-=10
                    speed2+=10
                print(speed1)
                print(speed2)
        elif event_.type == pygame.JOYBUTTONUP:
            mc.stop_motor(motor_id)
            mc.stop_motor(motor_id1)
            mc.stop_motor(motor_id2)
            mc.stop_motor(motor_id3)
            #print(joystick.get_hat(0))
#            print(joystick.get_axis(0))
'''
#vid.release()
#cv2.destroyAllWindows()
def go_forward():
    mc.move_motor(motor_id,speed2)#back right
    mc.move_motor(motor_id1,speed2)#back left
    mc.move_motor(motor_id2,speed2)#front right
    mc.move_motor(motor_id3,speed2)#front left
    
def go_backward():
    mc.move_motor(motor_id,speed1)#back right
    mc.move_motor(motor_id1,speed1)#back left
    mc.move_motor(motor_id2,speed1)#front right
    mc.move_motor(motor_id3,speed1)#front left
    
def turn_left():
    mc.move_motor(motor_id,speed1)#back right
    mc.move_motor(motor_id1,speed2)#back left
    mc.move_motor(motor_id2,speed1)#front right
    mc.move_motor(motor_id3,speed2)#front left

def turn_right():
    mc.move_motor(motor_id,speed2)#back right
    mc.move_motor(motor_id1,speed1)#back left
    mc.move_motor(motor_id2,speed2)#front right
    mc.move_motor(motor_id3,speed1)#front left

# Move motor with the given ID at your set speed 
#mc.move_motor(motor_id,speed1)      
#mc.move_motor(motor_id1,speed1)
#mc.move_motor(motor_id2,speed1)
#mc.move_motor(motor_id3,speed1)  




