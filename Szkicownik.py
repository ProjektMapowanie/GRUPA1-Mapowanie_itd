import serial as serial
import sys, random
import time
sensorData = serial.Serial('COM4',9600)     #115200)

while(1):
    while(sensorData.inWaiting()==0): # Wait here untill there is data on the Serial Port
            pass                          # Do nothing, just loop until data arrives
    textline = sensorData.readline()     # read the entire line of text
    print textline#, dataNums[2], dataNums[4]  # Make variables for Red, Blue, Green. Remember
