import json
import time
from AWS import init, insert
from sx126x import sx126x

# main loop
def main():
    init()
    node = sx126x(serial_num="/dev/ttyS0", freq=915, addr=65535,
                  power=22, rssi=True, air_speed=2400, relay=False)

    print("Waiting for messages");
    while True:
        message = node.receive()
        if message != None and len(message) > 0:
            for line in message.splitlines():
                print(line)
                fire = json.loads(line)
                print(fire)
                insert(fire)
        time.sleep(0.1)


if __name__ == '__main__':
    try:
        main()
        pass
    except KeyboardInterrupt:
        pass
