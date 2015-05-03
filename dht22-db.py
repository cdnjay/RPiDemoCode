#!/usr/bin/python

#Import libraries
import MySQLdb
import sys
import Adafruit_DHT

#Set sensor
sensor = Adafruit_DHT.DHT22
#Set GPIO pin
pin = 4

#Grab reading from sensor and set to variables
humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)

# Open database connection
db = MySQLdb.connect("localhost","root","password","database" )

# prepare a cursor object using cursor() method
cursor = db.cursor()

# Prepare SQL query to INSERT a record into the database.
sql = "INSERT INTO table(temp, humidity) \
       VALUES ('%s', '%s')" % \
       (temperature, humidity)
try:
   # Execute the SQL command
   cursor.execute(sql)
   # Commit your changes in the database
   db.commit()
except:
   # Rollback in case there is any error
   db.rollback()

# disconnect from server
db.close()
