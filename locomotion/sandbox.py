#!/usr/bin/env python

import datetime
import os
import sys
import threading
import time
import traceback
import signal
from iotools import IOTools


class Logger(object):
    def __init__(self, onRobot):
        self.useTerminal = not onRobot
        self.terminal = sys.stdout
        self.log = 0
        if os.path.isdir('/tmp/sandbox'):
            self.log = open('/tmp/sandbox/log.txt', 'a+')

    def write(self, message):
        if self.useTerminal:
            self.terminal.write(message)
        if self.log:
            self.log.write(message)
            self.log.flush()

    def flush(self):
        pass


class Sandbox:
    __version = '2018a'

    def __init__(self, onRobot):
        print(datetime.datetime.now())
        print('[Sandbox] R:SS Sandbox ' + Sandbox.__version)

        def signal_handler(signal, frame):
            print('[INFO] [Sandbox] Received signal no. {}'.format(signal))
            self.destroy()
            sys.exit(0)

        signal.signal(signal.SIGINT, signal_handler)
        signal.signal(signal.SIGTERM, signal_handler)

        self.__done = False
        self.__IO = IOTools(onRobot)

        try:
            def led_control_d():
                """
                This is the LED control *daemon* thread target.
                """
                ifkit = self.__IO.interface_kit
                led = ifkit.led

                # Blink all LEDs 3 times
                for _ in range(3):
                    for i in range(3):
                        ifkit.setOutputState(i, 1)
                    time.sleep(0.15)
                    for i in range(3):
                        ifkit.setOutputState(i, 0)
                    time.sleep(0.15)

                t = 0

                # Start heartbeat
                while not self.__done:
                    t = (t + 1) % 100
                    for i in range(3):
                        led._status[i] = ((t + led._ofs[i]) % led._mod[i] == 0) and led._val[i] and bool(led._rep[i])
                        led._rep[i] = led._rep[i] - int(led._rep[i] > 0 and led._status[i])
                        ifkit.setOutputState(i, led._status[i])
                    time.sleep(0.15)

            def toddler_control():
                """
                This is the toddler *control* thread target.
                """
                while not self.__done:
                    self.__toddler.control()

            def toddler_vision():
                """
                This is the toddler *vision* thread target.
                """
                while not self.__done:
                    self.__toddler.vision()

            sys.path.insert(0, '/home/student/')
            sys.path.insert(1, '/home/pi/')
            import toddler

            self.__toddler = toddler.Toddler(self.__IO)

            try:
                self.__led_control_d = threading.Thread(target=led_control_d)
                self.__toddler_control = threading.Thread(target=toddler_control)
                self.__toddler_vision = threading.Thread(target=toddler_vision)

                self.__led_control_d.setDaemon(True)

                self.__led_control_d.start()
                self.__toddler_control.start()
                self.__toddler_vision.start()

                while threading.active_count() > 0:
                    time.sleep(1)
            except KeyboardInterrupt:
                print('[INFO] [Sandbox] You pressed Ctrl+C!')
                self.destroy()
                sys.exit(0)
        except Exception:
            print('[ERROR] [Sandbox] The toddler is hurt:')
            traceback.print_exc()

    def destroy(self):
        self.__done = True
        self.__toddler_control.join()
        self.__toddler_vision.join()
        self.__IO.destroy()


if __name__ == '__main__':
    onRobot = bool(sys.argv.count('-rss'))
    sys.stdout = Logger(onRobot)
    sys.stderr = sys.stdout
    sandbox = Sandbox(onRobot)
