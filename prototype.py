import time
from mq2 import init, readCO2
from TempHumid import readTemp, readHumid

#main loop
def main():
         init()
         print("please wait for sensors to warm up...")
         time.sleep(20)
         while True:
                  COlevel = readCO2()
                  print("Current Voltage = " +str("%.2f"%(COlevel))+" V")
                  
                  print("Temperature: {}*C  Humidity: {}% ".format(readTemp(), readHumid()))
                  
                  if (COlevel > 1.8):
                      print("Fire detected!!!!")
                  else:
                      print("No fire :)")
                      
                  time.sleep(5)

if __name__ =='__main__':
         try:
                  main()
                  pass
         except KeyboardInterrupt:
                  pass
