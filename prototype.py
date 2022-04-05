import time
from mq2 import init as initmq2, readCO2
from TempHumid import measure, init as inittemp

#main loop
def main():
         initmq2()
         inittemp()
         print("please wait for sensors to warm up...")
         time.sleep(20)
         while True:
                  COlevel = readCO2()
                  print("Current Voltage = " +str("%.2f"%(COlevel))+" V")
                  
                  temp, humid  = measure()
                  print("Temperature: {}*C  Humidity: {}% ".format(temp, humid))
                  
                  if (COlevel > 1.8):
                      print("Fire detected!!!!")
                  else:
                      print("No fire :)")
                      
                  time.sleep(3.0)

if __name__ =='__main__':
         try:
                  main()
                  pass
         except KeyboardInterrupt:
                  pass
