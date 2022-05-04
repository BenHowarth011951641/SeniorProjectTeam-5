#!/usr/bin/env python3
import serial
import time
import time
import json
from datetime import datetime
from sx126x import sx126x
def main():
    node = sx126x(serial_num="/dev/ttyS0", freq=915, addr=3,
                  power=22, rssi=True, air_speed=2400, relay=False)

    print("please wait for sensors to warm up...")
    time.sleep(0)
    while True:
        line = ser.readline().decode('utf-8').rstrip() 
        gas = float(line[0:3])
        humid = float(line[8:13])
        temp = float(line[3:8])
        time.sleep(1.0)      
        co2level = (gas/1024)*3
        print("Current Voltage = " + str("%.2f" % (co2level))+" V")

       
        print("Temperature: {}C  Humidity: {}% ".format(temp, humid))

        #if (gas > 3.5):
            #print("Fire detected!!!!")
        #else:
            #print("No fire :)")

        fire = {
            "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "station": node.addr,
            "temp": temp,
            "humid": humid,
            "colevel": round(co2level, 2)
        }

        print(json.dumps(fire))
        node.sendMessage(2, json.dumps(fire))
        

if __name__ == '__main__' :       
    ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1) 
    ser.reset_input_buffer()
    while True:
        if ser.in_waiting > 0:              
            line = ser.readline().decode('utf-8').rstrip() 
            gas = float(line[0:3])
            humid = float(line[8:13])
            temp = float(line[3:8])
            time.sleep(2.0)
            try:
                main()           
                pass
            except KeyboardInterrupt:
                pass
