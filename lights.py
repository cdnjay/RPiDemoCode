#!/usr/bin/python

import RPi.GPIO as GPIO
import time
#import random

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

blue = 23
green = 18
amber = 13
red = 26

colours = [blue, green, amber, red]

for colour in colours:
        GPIO.setup(colour, GPIO.OUT)

count = 0

while count < 3:
        for colour in colours:
                GPIO.output(colour, 1)
                time.sleep(0.5)
        for colour in colours:
                GPIO.output(colour, 0)
                time.sleep(0.5)
        count += 1

#time.sleep(random.uniform(5, 10))

GPIO.cleanup()
