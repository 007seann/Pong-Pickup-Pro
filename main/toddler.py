#!/usr/bin/env python

import time


class Toddler:
    __version = '2018a'

    def __init__(self, IO):
        print('[Toddler] I am toddler {} playing in a sandbox'.format(Toddler.__version))

        self.camera = IO.camera.initCamera('pi', 'low')
        self.getInputs = IO.interface_kit.getInputs
        self.getSensors = IO.interface_kit.getSensors
        self.mc = IO.motor_control
        self.sc = IO.servo_control

    def control(self):
        print('{}\t{}'.format(self.getSensors(), self.getInputs()))

        self.mc.setMotor(2, 100 if self.getSensors()[0] >= 500 else -100)
        self.mc.setMotor(4, 100 if self.getSensors()[0] >= 500 else -100)

        self.sc.engage()
        self.sc.setPosition(0 if self.getSensors()[0] >= 500 else 180)

        time.sleep(0.05)

    def vision(self):
        image = self.camera.getFrame()
        self.camera.imshow('Camera', image)
