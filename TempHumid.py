import time
import board
import adafruit_dht
import psutil

sensor = None

def init():
    global sensor
    #kills previously running process.
    for proc in psutil.process_iter():
        if proc.name() == 'libgpiod_pulsein' or proc.name() == 'libgpiod_pulsei':
            proc.kill()

    #output pin on pi that sensor is connected to.        
    sensor = adafruit_dht.DHT11(board.D23)

def measure():
    global sensor
    
    sensor.measure()
    temp = sensor._temperature
    humidity = sensor._humidity
    
    return temp, humidity

#Displays temperature/humiduty data or shows an error.
def main():
    init()
    while True:
        try:
            temp = sensor.temperature
            humidity = sensor.humidity
            print("Temperature: {}*C  Humidity: {}% ".format(temp, humidity))

        except RuntimeError as error:
            print(error.args[0])
            time.sleep(2.0)
            continue
        
        except Exception as error:
            sensor.exit()
            raise error
    
        time.sleep(2.0)
    
if __name__ =='__main__':
         try:
                  main()
                  pass
         except KeyboardInterrupt:
                  pass