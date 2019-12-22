import RPi.GPIO as GPIO
import time
import subprocess
button=3
GPIO.setmode(GPIO.BCM)
GPIO.setup(button,GPIO.IN,pull_up_down=GPIO.PUD_UP)
while True:
    if GPIO.input(button)==0:
        print("Pressed")
        exec(open("cam.py").read())
        time.sleep(0.5)

        
    
