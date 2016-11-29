import myLib ,damatu
from PIL import ImageGrab, Image
import numpy as np
import cv2 ,pyautogui, datetime, time, threading, requests
from io import BytesIO as StringIO
import configparser ,json ,zipfile ,os ,sys

area_grab =[500 ,60 ,1400 ,750]
s_checkTime = (0, 0, 1920, 1080)

time.sleep(5)
timeTarget = Image.open(r'rsc\check_main_kick.PNG')
# timeTarget = Image.open(r'rsc\check_main_kick.png')
timeTarget = cv2.cvtColor(np.array(timeTarget, dtype=np.uint8), cv2.COLOR_RGBA2GRAY)
screen = ImageGrab.grab(area_grab)
screen = cv2.cvtColor(np.array(screen, dtype=np.uint8), cv2.COLOR_RGB2GRAY)
res = cv2.matchTemplate(screen, timeTarget, myLib.method)
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
if max_val > 0.99:
    print(1)