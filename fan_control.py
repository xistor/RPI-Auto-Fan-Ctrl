import fan
import time
import os

FAN_EN = 18 # GPIO (BCM)

MIN_TEMP = 40.0
ADJ_TEMP = 50.0
MAX_TEMP = 70.0

FAN_LOW = 65
FAN_HIGH = 100
FAN_OFF = 0

piFan = fan.Fan(FAN_EN)
piFan.start()

def getCpuTemperature():
    res = os.popen('vcgencmd measure_temp').readline()
    temp =(res.replace("temp=","").replace("'C\n",""))
    #print("temp is {0}".format(temp))
    return float(temp)

while True:
    time.sleep(30)
    temp = getCpuTemperature()
    speed = FAN_LOW + (FAN_HIGH - FAN_LOW) * ((temp - MIN_TEMP) / (MAX_TEMP - MIN_TEMP))
    #print("Speed : {}".format(speed))

    if temp < MIN_TEMP:
        piFan.setSpeed(0)
        #print("stop")
    elif temp > MAX_TEMP:
        piFan.setSpeed(100)
        #print("MAX")
    elif temp > ADJ_TEMP:
        piFan.setSpeed(speed)
        #print("adj")
    

