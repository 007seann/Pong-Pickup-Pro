
import socket 
import sys 
from motors import Motors 
from time import time, sleep 
import RPi.GPIO as GPIO

TRIG = 24
ECHO = 23


ip = '10.0.0.10'
port = 65432

mc = Motors() 

motor_id = 0
motor_id1 = 1 # The port that your motor is plugged in to
motor_id2 = 2
motor_id3 = 3 
straightSpeed = 65# forward = positive, backwards = negative
turnSpeed = 60
k = 1.75
run_time = 30        # number of seconds to run motors

in1 = 17
in2 = 18
in3 = 27
in4 = 22

# careful lowering this, at some point you run into the mechanical limitation of how quick your motor can move
step_sleep = 0.002

step_count = int(1* (1024))  # 5.625*(1/64) per step, 4096 steps is 360°

direction = True # True for clockwise, False for counter-clockwise

# defining stepper motor sequence (found in documentation http://www.4tronix.co.uk/arduino/Stepper-Motors.php)
step_sequence = [[1,1,0,0],
                 [0,1,1,0],
                 [0,0,1,1],
                 [1,0,0,1]]

# setting up
GPIO.setmode( GPIO.BCM )
GPIO.setup(in1, GPIO.OUT )
GPIO.setup(in2, GPIO.OUT )
GPIO.setup(in3, GPIO.OUT )
GPIO.setup(in4, GPIO.OUT )

# initializing
GPIO.output(in1, GPIO.LOW )
GPIO.output(in2, GPIO.LOW )
GPIO.output(in3, GPIO.LOW )
GPIO.output(in4, GPIO.LOW )

motor_pins = [in1,in2,in3,in4]
motor_step_counter = 0

def turn_time(theta):
    return 2.50*theta/360 


def spin_360():
    mc.move_motor(motor_id,-68)#back right
    mc.move_motor(motor_id1,68)#back left
    mc.move_motor(motor_id2,-68)#front right
    mc.move_motor(motor_id3, 68)#front left
    sleep(1)
    mc.stop_motor(motor_id)
    mc.stop_motor(motor_id1)
    mc.stop_motor(motor_id2)
    mc.stop_motor(motor_id3)
    sleep(0.5)
    mc.move_motor(motor_id,-68)#back right
    mc.move_motor(motor_id1,68)#back left
    mc.move_motor(motor_id2,-68)#front right
    mc.move_motor(motor_id3, 68)#front left
    sleep(1)
    mc.stop_motor(motor_id)
    mc.stop_motor(motor_id1)
    mc.stop_motor(motor_id2)
    mc.stop_motor(motor_id3)
    mc.move_motor(motor_id,-68)#back right
    mc.move_motor(motor_id1,68)#back left
    mc.move_motor(motor_id2,-68)#front right
    mc.move_motor(motor_id3, 68)#front left
    sleep(1)
    mc.stop_motor(motor_id)
    mc.stop_motor(motor_id1)
    mc.stop_motor(motor_id2)
    mc.stop_motor(motor_id3)


def go_forward(suction=False):
    # start moving at high speed 
    mc.move_motor(motor_id,straightSpeed)#back right
    mc.move_motor(motor_id1,straightSpeed)#back left
    mc.move_motor(motor_id2,straightSpeed)#front right
    mc.move_motor(motor_id3,straightSpeed)#front left
    sleep(0.45)
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
    sleep(0.3)
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
    
    sleep(0.3)
    
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

def spin_gate():
    global motor_step_counter
    
    for i in range(step_count):
        print("doing")
        for pin in range(0, len(motor_pins)):
            GPIO.output( motor_pins[pin], step_sequence[motor_step_counter][pin] )
        if direction==True:
            motor_step_counter = (motor_step_counter - 1) % 4
        elif direction==False:
            motor_step_counter = (motor_step_counter + 1) % 4
        else: # defensive programming
            print( "uh oh... direction should *always* be either True or False" )
            cleanup()
        sleep(step_sleep)

'''
mc.stop_motor(0)
mc.stop_motor(1)
mc.stop_motor(2)
mc.stop_motor(3)
mc.stop_motor(4)
'''
# mc.move_motor(0,100)
# sleep(2)
# mc.stop_motor(0)
'''
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    checked_ball_360 = False
    spinCount = 0
    no_ball_count = 0
    s.bind((ip, port))
    s.listen()
    conn, addr = s.accept()
    with conn:
        while True:
            sleep(0.5)
            data = conn.recv(1024)
            instruction = data.decode('utf-8')
            print(instruction)
            if (instruction[0]=='3'):
                no_ball_count+=1
            if (instruction[0]=='0'):
                mc.stop_motor(0)
                mc.stop_motor(1)
                mc.stop_motor(2)
                mc.stop_motor(3)
                turn_left()
                no_ball_count = 0
                spinCount=0
                #print("left")
                checked_ball_360 = False
            if (instruction[0]=='2'):
                mc.stop_motor(0)
                mc.stop_motor(1)
                mc.stop_motor(2)
                mc.stop_motor(3)
                turn_right()
                no_ball_count = 0
                checked_ball_360 = False
                spinCount = 0
                #print("right")
            if (instruction[0]=='1'):
                mc.stop_motor(0)
                mc.stop_motor(1)
                mc.stop_motor(2)
                mc.stop_motor(3)
                go_forward()
                count = 0
                #print("forward")
                #pass
                checked_ball_360 = False
                spinCount=0
            elif (no_ball_count==5 and spinCount < 5):
                mc.stop_motor(0)
                mc.stop_motor(1)
                mc.stop_motor(2)
                mc.stop_motor(3)
                mc.move_motor(motor_id,-68)#back right
                mc.move_motor(motor_id1,68)#back left
                mc.move_motor(motor_id2,-68)#front right
                mc.move_motor(motor_id3, 68)#front left
                sleep(2)
                mc.stop_motor(motor_id)
                mc.stop_motor(motor_id1)
                mc.stop_motor(motor_id2)
                mc.stop_motor(motor_id3)
                spinCount+=1
                continue

'''
#go_forward()
#turn_left()
#turn_right()

#spin_360()
'''
#print("here")
mc.move_motor(0, 100)
sleep(10)
mc.stop_motor(0)
#mc.move_motor(1, 100)
#sleep(10)
#mc.stop_motor(1)
spin_gate()
for i in range(1, 21):
    mc.move_motor(1, i*5)
    sleep(0.25)
#mc.stop_motor(1)

print("end")
'''

#spin_gate()
#sleep(2)
#spin_gate()
#for i in range(1, 21):
#    mc.move_motor(0, i*5)
#    sleep(0.25)


#sleep(2)
'''

#for i in range(1, 11):
    #mc.move_motor(0,100-(i*10))
    #sleep(0.5)

#sleep(2)
mc.stop_motor(0)

#sleep(10)

#go_forward()

#mc.stop_motor(0)


'''
#go_forward()
#mc.move_motor(4, 100)
#sleep(5)
#mc.stop_motor(4)
#spin_360()

#spin_360()
'''
'''
'''

mc.move_motor(0, 70)
sleep(1)
mc.move_motor(0, 50)
sleep(1)
mc.move_motor(0, 30)
sleep(1)
mc.move_motor(0, 25)
sleep(1)
mc.stop_motor(0)
mc.stop_motor(1)

'''
mc.stop_motor(1)
mc.move_motor(0, 100)
sleep(10)
mc.stop_motor(0)
