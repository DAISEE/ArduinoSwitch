#!/usr/bin/env python

 
import time   
import json
import pathlib
import requests
import serial

ser = serial.Serial('/dev/ttyACM0', 9600)

relai1_status = 0
relai2_status = 0
relai3_status = 0
relai4_status = 0

def turnOn(relai):
    if(relai == "1"):
        if relai_status == 0:
            ser.write(str("1").encode())
            print ("Turn 1 on")
            relai1_status = 1
    if(relai == "2"):
        if relai2_status == 0:
            ser.write(str("2").encode())
            print ("Turn 2 on")
            relai2_status = 1
    if(relai == "3"):
        if relai3_status == 0:
            ser.write(str("3").encode())
            print ("Turn 3 on")
            relai3_status = 1
    if(relai == "3"):
        if relai3_status == 0:
            ser.write(str("3").encode())
            print ("Turn 3 on")
            relai3_status = 1
    if(relai == "4"):
        if relai4_status == 0:
            ser.write(str("4").encode())
            print ("Turn 4 on")
            relai4_status = 1




def turnOff(relai):
    if(relai == "1"):
        if relai_status == 1:
            ser.write(str("1").encode())
            print ("Turn 1 off")
            relai1_status = 0
    if(relai == "2"):
        if relai2_status == 1:
            ser.write(str("2").encode())
            print ("Turn 2 off")
            relai2_status = 0
    if(relai == "3"):
        if relai3_status == 1:
            ser.write(str("3").encode())
            print ("Turn 3 off")
            relai3_status = 0
    if(relai == "3"):
        if relai3_status == 1:
            ser.write(str("3").encode())
            print ("Turn 3 off")
            relai3_status = 0
    if(relai == "4"):
        if relai4_status == 1:
            ser.write(str("4").encode())
            print ("Turn 4 off")
            relai4_status = 0


def getEnergySum(t0,t1):
    sum=0
    headers = {'Content-Type': 'application/json',}
    data = 'login=debian&password=debian'
    #t0 = time.time() - 10
    #t1 = time.time()

    result = requests.post('http://192.168.0.21:8080/api/4/get/watts/by_time/'+str(t0)+'/'+str(t1), headers=headers, data=data)
    parsed_json = json.loads(result.text)
    print(parsed_json['data'][0]['value'])

    for n in range(0,len(parsed_json['data'])):
        print(parsed_json['data'][n]['value'])
        sum = sum + parsed_json['data'][n]['value']

    print(str(sum))

