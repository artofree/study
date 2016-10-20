import damatu as td
import myLib ,damatu
from PIL import ImageGrab, Image
import numpy as np
import cv2 ,pyautogui, datetime, time, threading, requests
from io import BytesIO as StringIO
import configparser ,json ,zipfile ,os

gindex =0
def fun():
    # gindex =1
    print(gindex)

fun()

# lock = threading.Lock()
#
# def Thread1():
#     time.sleep(5)
#     print('thread1')
#
# def Thread2():
#     lock.acquire()
#     try:
#         print('thread2')
#     finally:
#         lock.release()
#
#
# t1 = threading.Thread(target=Thread1)
# t1.start()
# time.sleep(1)
# myLib.stop_thread(t1)
# t2 = threading.Thread(target=Thread2)
# t2.start()

# import myThread
#
# myThread.beginWork()
# time.sleep(10)
# myThread.clearWork()

# time.sleep(5)
# theConf =myLib.myConf()
# pyautogui.click(theConf.coor_login_closefirstpage)
# print(myLib.check_img(theConf.check_login_against))
# cf = configparser.ConfigParser()
# cf.read(r"rsc\conf")
# scns =cf.sections()
# print(scns)
# print(cf.options('login'))
# print(cf.items('login'))
# theTuple =cf.get('login' ,'thread')
# theTuple =json.loads(theTuple)
# print(type(theTuple))