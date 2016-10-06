#!/usr/bin/env python

import serial  
import time   
from pathlib import Path

ser = serial.Serial('/dev/ttyACM0', 9600)

"""File X exist: 
relay X is closed (with energy flowing). 
File does not exist: relay X is open (no energy flowing)
"""
my_file1 = Path("/home/debian/one")
my_file2 = Path("/home/debian/two")
my_file3 = Path("/home/debian/three")
my_file4 = Path("/home/debian/four")


my_file1_status = 0
my_file2_status = 0
my_file3_status = 0
my_file4_status = 0



while True:     

    if my_file1.is_file():
        if my_file1_status == 0:
            ser.write(str("1").encode())
            print ("Turn 1 on")
            my_file1_status = 1
         
    else:    
        if my_file1_status == 1:
            ser.write(str("1").encode())
            print ("Turn 1 off")
            my_file1_status = 0
         
    if my_file2.is_file():
        if my_file2_status == 0:
            ser.write(str("2").encode())
            print ("turn 2 on")
            my_file2_status = 1
         
    else:    
        if my_file2_status == 1:
            ser.write(str("2").encode())    
            print ("turn 2 off")
            my_file2_status = 0
        
    if my_file3.is_file():
        if my_file3_status == 0:
            ser.write(str("3").encode())
            print ("turn 3 on")
            my_file3_status = 1
         
    else:    
        if my_file3_status == 1:
            ser.write(str("3").encode())    
            print ("turn 3 off")
            my_file3_status = 0

    if my_file4.is_file():
        if my_file4_status == 0:
            ser.write(str("4").encode())
            print ("turn 4 on")
            my_file4_status = 1
         
    else:    
        if my_file4_status == 1:
            ser.write(str("4").encode())    
            print ("turn 4 off")
            my_file4_status = 0
    
    
    
        
