import time
from AWS import init, insert
from sx126x import sx126x

# main loop
def main():
    init()
    node = sx126x(serial_num="/dev/ttyS0", freq=915, addr=1,
                  power=22, rssi=True, air_speed=2400, relay=False)

    while True:
        message = node.receive()
        if message != None and len(message) > 0:
            print(message)
        time.sleep(0.1)


if __name__ == '__main__':
    try:
        main()
        pass
    except KeyboardInterrupt:
        pass
