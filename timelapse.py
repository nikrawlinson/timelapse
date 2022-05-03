import time
import os
import ftplib
from datetime import datetime
from gpiozero import MotionSensor
from picamera import PiCamera
from ftplib import FTP

pir = MotionSensor(4)
    
def thegrab():
    thetime = datetime.now()
    detectiontime = thetime.strftime("%y-%m-%d-%H-%M-%S")
    extension = ".jpg"
    filename = detectiontime + extension
    camera = PiCamera()
    #camera.rotation = 270
    time.sleep(2)
    camera.capture(filename)
    camera.close()
    ftp = FTP('[server address]')
    ftp.login('[username]','[password]')
    ftp.cwd('')
    ftp.storbinary("STOR " + filename, open(filename, 'rb'))
    ftp.quit()
    os.remove(filename)
    
while True:
    pir.wait_for_motion()
    thegrab()
    time.sleep(30)
