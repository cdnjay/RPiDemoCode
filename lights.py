#!/usr/bin/python

#Import required libraries
import RPi.GPIO as GPIO
import time

#Setup GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

#Set GPIO pins
blue = 23
green = 18
amber = 13
red = 26

#Create array of LED's
colours = [blue, green, amber, red]

#Set GPIO pins as output
for colour in colours:
        GPIO.setup(colour, GPIO.OUT)

#Declare variable
count = 0

#Turn on and off LED's
while count < 3:
        for colour in colours:
                GPIO.output(colour, 1)
                time.sleep(0.5)
        for colour in colours:
                GPIO.output(colour, 0)
                time.sleep(0.5)
        count += 1

#Cleanup GPIO pins
GPIO.cleanup()
