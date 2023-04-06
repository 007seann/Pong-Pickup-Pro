#!/usr/bin/env python

import psutil
import subprocess
from gpiozero import Button


def shutdown():
    print('[rss-supervisor] Shutting down...')
    subprocess.check_call(['sudo', 'poweroff'])


if __name__ == '__main__':
    button = Button(21, hold_time=2)
    button.when_held = shutdown

    sandbox_p = None
    sandbox_pid = None
    sandbox_running = False

    sandbox_script = '/usr/local/bin/sandbox.py'
    command = ['python', sandbox_script, '-rss']

    while True:
        button.wait_for_press()
        button.wait_for_release()

        for process in psutil.process_iter():
            if process.cmdline() == command:
                print('[rss-supervisor] Process found. Terminating it.')
                process.terminate()
                break
        else:
            print('[rss-supervisor] Process not found: starting it.')
            subprocess.Popen(command, shell=False)
