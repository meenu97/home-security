from gpiozero import MotionSensor
import time 
import os
import numpy as np
import cv2
from url import url
from facedetection import facedetect
 
pir = MotionSensor(4)

while 1: 
    pir.wait_for_motion()
    print("Motion detected")
    url()
    facedetect()
    print("back in main")
    pir.wait_for_no_motion()
