import RPi.GPIO as GPIO
import time

class Fan:
    def __init__(self, EN):
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        self.EN = EN
        GPIO.setup(EN,GPIO.OUT,initial=GPIO.LOW)

        GPIO.setup(EN,GPIO.OUT)
        self.pEN = GPIO.PWM(EN,75)
        self.pEN.start(0)

    def start(self):
        time.sleep(1)
        self.pEN.ChangeDutyCycle(100)
        GPIO.output(self.EN,True)

    def setSpeed(self, speed):
        time.sleep(1)
        self.pEN.ChangeDutyCycle(speed)
        GPIO.output(self.EN,True)
