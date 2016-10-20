import myLib ,damatu
from PIL import ImageGrab, Image
import numpy as np
import cv2 ,pyautogui, datetime, time, threading, requests
from io import BytesIO as StringIO
import configparser ,json ,zipfile ,os

threadList =[]
servUrl ='http://139.219.238.37:8000/'
theConf =myLib.myConf()
timeStamp = 0


def getTimeStamp():
    global timeStamp
    while 1:
        timeStamp =float(requests.get(url=servUrl +'getTimeStamp').text)
        timeStamp =round(timeStamp ,2)
        time.sleep(0.2)

def login():
    global theConf
    pyautogui.click(theConf.coor_login_checkie)
    time.sleep(3)
    pyautogui.click(theConf.coor_login_agree)
    time.sleep(3)

####################################################################################

def mainWork():
    ###1.线程-常规终端只开获得时间戳
    timeStampThread = threading.Thread(target=getTimeStamp)
    timeStampThread.start()
    threadList.append(timeStampThread)



def beginWork():
    t = threading.Thread(target=mainWork)
    t.start()
    threadList.append(t)

def endWork():
    for t in threadList:
        myLib.stop_thread(t)