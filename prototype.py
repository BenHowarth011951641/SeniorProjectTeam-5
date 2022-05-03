import time
import json
from datetime import datetime
from mq2 import init as initmq2, readCO2
from TempHumid import measure, init as inittemp
from sx126x import sx126x

# main loop
def main():
    initmq2()
    inittemp()
    node = sx126x(serial_num="/dev/ttyS0", freq=915, addr=2,
                  power=22, rssi=True, air_speed=2400, relay=False)

    print("please wait for sensors to warm up...")
    time.sleep(0)
    while True:
        COlevel = readCO2()
        print("Current Voltage = " + str("%.2f" % (COlevel))+" V")

        temp, humid = measure()
        print("Temperature: {}C  Humidity: {}% ".format(temp, humid))

        #if (COlevel > 3.5):
            #print("Fire detected!!!!")
        #else:
            #print("No fire :)")

        fire = {
            "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "station": node.addr,
            "temp": temp,
            "humid": humid,
            "colevel": round(COlevel, 2)
        }

        print(json.dumps(fire))
        node.sendMessage(2, json.dumps(fire))
        time.sleep(1.0)


if __name__ == '__main__':
    try:
        main()
        pass
    except KeyboardInterrupt:
        pass