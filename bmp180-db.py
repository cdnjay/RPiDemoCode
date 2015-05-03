#!/usr/bin/python

import MySQLdb
import sys
import Adafruit_BMP.BMP085 as BMP085

sensor = BMP085.BMP085(mode=BMP085.BMP085_ULTRAHIGHRES)

temperature = format(sensor.read_temperature())
pressure = format(sensor.read_pressure())

#print temperature
#print pressure

# Open database connection
db = MySQLdb.connect("localhost","root","password","database" )

# prepare a cursor object using cursor() method
cursor = db.cursor()

# Prepare SQL query to INSERT a record into the database.
sql = "INSERT INTO table(temp, pressure) \
       VALUES ('%s', '%s')" % \
       (temperature, pressure)
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
