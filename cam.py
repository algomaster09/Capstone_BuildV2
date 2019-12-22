import subprocess

from picamera import PiCamera
from time import sleep

camera = PiCamera()
camera.start_preview()
sleep(5)
camera.capture('picture.jpg')
camera.stop_preview()
exec(open("dist.py").read())
exec(open("main.py").read())