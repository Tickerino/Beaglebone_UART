#!/usr/bin/python
import Adafruit_BBIO.UART as UART
import serial

UART.setup("UART2")

ser = serial.Serial(port = "/dev/ttyO2", baudrate = 9600)
ser.close()
ser.open()
if ser.isOpen():
        print "Serial2 is open!"
        ser.write("Hello World!from 2")
ser.close()






