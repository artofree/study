import myLib, damatu, sys, socket
from PIL import ImageGrab, Image
import numpy as np
import cv2, pyautogui, datetime, time, threading, requests
from io import BytesIO as StringIO
import configparser, json, zipfile, os

threadList = []
decodeThreadList = []
theCodeDict = {}
servUrl = 'http://139.219.238.37:8000/'
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
code_url = os.path.join(os.path.join(BASE_DIR, 'rsc'), 'code.png')
theConf = myLib.myConf()

timeStamp = 0
lock = threading.Lock()

###第一步，用hostname获得拍牌人信息
hostName = socket.gethostname()
orderid, orderpass, identy = requests.get(url=servUrl + 'getOrderInfo' ,data={'hostname': hostName}).text.split('-')


def getCode():
    global theCodeDict
    dmt = damatu.DamatuApi("slientcraft", "inwcwizard")
    theCode = dmt.decode(code_url, 200)
    lock.acquire()
    try:
        if theCode in theCodeDict:
            theCodeDict[theCode] += 1
        else:
            theCodeDict[theCode] = 1
    finally:
        lock.release()
    time.sleep(20)


def deCode(area_code):
    global theCodeDict
    global decodeThreadList
    code = ImageGrab.grab(area_code)
    code.save(code_url, "PNG")
    time.sleep(1)
    for i in range(10):
        t = threading.Thread(target=getCode)
        t.start()
        decodeThreadList.append(t)
    time.sleep(10)
    if 'ERROR' in theCodeDict:
        theCodeDict.pop('ERROR')
    if 'IERROR' in theCodeDict:
        theCodeDict.pop('IERROR')
    theCodeDict = sorted(theCodeDict.items(), key=lambda dic: dic[1])
    for t in decodeThreadList:
        myLib.stop_thread(t)
    decodeThreadList =[]
    theCode = theCodeDict[-1][0]
    theCodeDict = {}
    return theCode


def getTimeStamp():
    global timeStamp
    while 1:
        timeStamp = float(requests.get(url=servUrl + 'getTimeStamp').text)
        timeStamp = round(timeStamp, 2)
        time.sleep(0.2)

def against():
    while 1:
        if myLib.check_img(theConf.check_main_kick):
            pyautogui.click(theConf.coor_login_orderid)
            time.sleep(1)
            login()
        time.sleep(10)

def preLogin():
    pyautogui.click(x=260, y=1060)
    time.sleep(5)
    pyautogui.click(theConf.coor_login_telcom)
    time.sleep(1)
    pyautogui.click(theConf.coor_login_closefirstpage)
    time.sleep(1)


def againstLogin():
    pyautogui.click(theConf.coor_login_orderid)
    time.sleep(1)
    pyautogui.typewrite(orderid)
    time.sleep(1)
    pyautogui.click(theConf.coor_login_orderpass)
    time.sleep(1)
    pyautogui.typewrite(orderpass)
    time.sleep(1)
    pyautogui.click(theConf.coor_login_identy)
    time.sleep(1)
    pyautogui.typewrite(identy)
    time.sleep(1)
    pyautogui.click(theConf.coor_login_againstcode)
    time.sleep(1)
    pyautogui.typewrite(deCode(theConf.area_login_againstcode))
    time.sleep(1)
    pyautogui.click(theConf.coor_login_againstlongin)
    time.sleep(5)


def login():
    pyautogui.click(theConf.coor_login_checkie)
    time.sleep(3)
    pyautogui.click(theConf.coor_login_agree)
    time.sleep(3)
    pyautogui.click(theConf.coor_login_orderid)
    time.sleep(1)
    pyautogui.typewrite(orderid)
    time.sleep(1)
    pyautogui.click(theConf.coor_login_orderpass)
    time.sleep(1)
    pyautogui.typewrite(orderpass)
    time.sleep(1)
    pyautogui.click(theConf.coor_login_code)
    time.sleep(1)
    pyautogui.typewrite(deCode(theConf.area_login_code))
    time.sleep(1)
    pyautogui.click(theConf.coor_login_longin)
    time.sleep(5)
    if myLib.check_img(theConf.check_login_against):
        pyautogui.click(theConf.coor_login_confirmagainst)
        time.sleep(1)
        againstLogin()


####################################################################################
###主线程
def mainWork():
    ###线程1-常规终端只开获得时间戳
    timeStampThread = threading.Thread(target=getTimeStamp)
    timeStampThread.start()
    threadList.append(timeStampThread)
    ###线程2-防t
    againstThread =threading.Thread(target=against)
    againstThread.start()
    threadList.append(againstThread)
    ###登陆：
    preLogin()
    login()


def beginWork():
    t = threading.Thread(target=mainWork)
    t.start()
    threadList.append(t)


def endWork():
    for t in threadList:
        myLib.stop_thread(t)
