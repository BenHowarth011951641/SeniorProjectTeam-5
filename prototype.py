import time
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
    time.sleep(20)
    while True:
        COlevel = readCO2()
        print("Current Voltage = " + str("%.2f" % (COlevel))+" V")

        temp, humid = measure()
        print("Temperature: {}C  Humidity: {}% ".format(temp, humid))

        if (COlevel > 1.8):
            print("Fire detected!!!!")
        else:
            print("No fire :)")

        message = "temperature: " + \
            str(temp) + " humidity: " + str(humid) + " CO2: " + str(COlevel)
        node.sendMessage(1, message)
        time.sleep(1.0)


if __name__ == '__main__':
    try:
        main()
        pass
    except KeyboardInterrupt:
        pass