import socket
import sys
from motors import Motors 
from time import time, sleep
import RPi.GPIO as GPIO

TRIG = 24
ECHO = 23

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.IN)
GPIO.setwarnings(False)
GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)
i = GPIO.input(17)

ip = '10.0.0.10'
port = 65432

mc = Motors() 

motor_id = 0
motor_id1 = 1 # The port that your motor is plugged in to
motor_id2 = 2
motor_id3 = 3
motor_id4 = 4
initialSpeed = 100
straightSpeed = 100# forward = positive, backwards = negative
turnSpeed = 60
k = 1.75
run_time = 30        # number of seconds to run motors


def turn_time(theta):
    return 2.50*theta/360 

def go_forward(suction=False):
    # start moving at high speed 
    mc.move_motor(motor_id,initialSpeed)#back right
    mc.move_motor(motor_id1,initialSpeed)#back left
    mc.move_motor(motor_id2,initialSpeed)#front right
    mc.move_motor(motor_id3,initialSpeed)#front left
    sleep(0.20)
    if suction: start_suction()
    mc.stop_motor(motor_id)
    mc.stop_motor(motor_id1)
    mc.stop_motor(motor_id2)
    mc.stop_motor(motor_id3)
    

    mc.move_motor(motor_id,straightSpeed)#back right
    mc.move_motor(motor_id1,straightSpeed)#back left
    mc.move_motor(motor_id2,straightSpeed)#front right
    mc.move_motor(motor_id3,straightSpeed)#front left
    sleep(0.4)
    #if i==0:
    mc.stop_motor(motor_id)
    mc.stop_motor(motor_id1)
    mc.stop_motor(motor_id2)
    mc.stop_motor(motor_id3)
    

def go_backward():
    mc.move_motor(motor_id,-straightSpeed)#back right
    mc.move_motor(motor_id1,-straightSpeed)#back left
    mc.move_motor(motor_id2,-straightSpeed)#front right
    mc.move_motor(motor_id3,-straightSpeed)#front left
    sleep(0.3)
    mc.stop_motor(motor_id)
    mc.stop_motor(motor_id1)
    mc.stop_motor(motor_id2)
    mc.stop_motor(motor_id3)
    
def turn_right():
    # start moving at high speed
    #mc.move_motor(motor_id,-initialSpeed)#back right
    #mc.move_motor(motor_id1,initialSpeed)#back left
    #mc.move_motor(motor_id2,-initialSpeed)#front right
    #mc.move_motor(motor_id3,initialSpeed)#front left
    #sleep(0.20)
    #mc.stop_motor(motor_id)
    #mc.stop_motor(motor_id1)
    #mc.stop_motor(motor_id2)
    #mc.stop_motor(motor_id3)
    #t = turn_time(theta)
    #sleep(t)
    mc.move_motor(motor_id,-100)#back right
    mc.move_motor(motor_id1,100)#back left
    mc.move_motor(motor_id2,-100)#front right
    mc.move_motor(motor_id3,100)#front left
    sleep(0.35)
    mc.stop_motor(motor_id)
    mc.stop_motor(motor_id1)
    mc.stop_motor(motor_id2)
    mc.stop_motor(motor_id3)
    
def turn_left():
    #mc.move_motor(motor_id,initialSpeed)#back right
    #mc.move_motor(motor_id1,-initialSpeed)#back left
    #mc.move_motor(motor_id2,initialSpeed)#front right
    #mc.move_motor(motor_id3,-initialSpeed)#front left
    #t = 1.06*turn_time(theta)
    #sleep(t)
    #sleep(0.2)
    #mc.stop_motor(motor_id)
    #mc.stop_motor(motor_id1)
    #mc.stop_motor(motor_id2)
    #mc.stop_motor(motor_id3)
    
    mc.move_motor(motor_id,100)#back right
    mc.move_motor(motor_id1,-100)#back left
    mc.move_motor(motor_id2,100)#front right
    mc.move_motor(motor_id3,-100)#front left
    
    sleep(0.35)
    
    mc.stop_motor(motor_id)
    mc.stop_motor(motor_id1)
    mc.stop_motor(motor_id2)
    mc.stop_motor(motor_id3)
    
def start_suction():
    mc.move_motor(4,100)#back right
    sleep(10)
    mc.stop_motor(4)
    
def return_fan(): 
    mc.move_motor(5,100)#back right
    sleep(3)
    mc.stop_motor(5)

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

mc.move_motor(0,100)
sleep(10)
mc.stop_motor(0)
'''
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((ip, port))
    s.listen()
    conn, addr = s.accept()
    with conn:
        while True:
            data = conn.recv(1024)
            instruction = data.decode('utf-8')
            print(instruction)
            
            if (instruction[0]=='0'):
                turn_left()
                count = 0
                #print("left")
            elif (instruction[0]=='2'):
                turn_right()
                count = 0
                #print("right")
            elif (instruction[0]=='1'):
                go_forward()
                count = 0
                #print("forward")
                #pass
'''
#go_forward()
#turn_left()
#turn_right()
