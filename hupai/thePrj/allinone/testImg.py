import myLib ,damatu
from PIL import ImageGrab, Image
import numpy as np
import cv2 ,pyautogui, datetime, time, threading, requests
from io import BytesIO as StringIO
import configparser ,json ,zipfile ,os ,sys

# area_grab =[500 ,60 ,1400 ,750]
area_grab =[1100 ,300 ,1250 ,350]
# area_grab =[640 ,455 ,730 ,490]
ver =1

time.sleep(5)
# timeTarget = Image.open(r'rsc\check_main_kick.PNG')
timeTarget = Image.open(r'rsc\87400.PNG')
timeTarget = cv2.cvtColor(np.array(timeTarget, dtype=np.uint8), cv2.COLOR_RGBA2GRAY)
while 1:
    print(datetime.datetime.now())
    screen = ImageGrab.grab(area_grab)
    screen = cv2.cvtColor(np.array(screen, dtype=np.uint8), cv2.COLOR_RGB2GRAY)
    print(datetime.datetime.now())
    res = cv2.matchTemplate(screen, timeTarget, myLib.method)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    print(datetime.datetime.now())
    time.sleep(10)
    if max_val > 0.95:
        print(1)
        break