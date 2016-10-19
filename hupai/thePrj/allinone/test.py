import damatu as td
import myLib ,damatu
from PIL import ImageGrab, Image
import numpy as np
import cv2 ,pyautogui, datetime, time, threading, requests
from io import BytesIO as StringIO
import configparser ,json

time.sleep(5)
theConf =myLib.myConf()
# pyautogui.click(theConf.coor_login_closefirstpage)
print(myLib.check_img(theConf.check_login_against))
# cf = configparser.ConfigParser()
# cf.read(r"rsc\conf")
# scns =cf.sections()
# print(scns)
# print(cf.options('login'))
# print(cf.items('login'))
# theTuple =cf.get('login' ,'thread')
# theTuple =json.loads(theTuple)
# print(type(theTuple))