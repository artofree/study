# # import damatu as td
import myLib ,damatu
from PIL import ImageGrab, Image
import numpy as np
import cv2 ,pyautogui, datetime, time, threading, requests
from io import BytesIO as StringIO
import configparser ,json ,zipfile ,os ,sys

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
#用于前期自动登陆打码
code_url = os.path.join(os.path.join(BASE_DIR, 'rsc'), 'code.png')


#检查当前价格区域
time.sleep(6)
screen = ImageGrab.grab((600, 450, 750, 500))
screen.show()


#检查对时区域
# time.sleep(6)
# s_checkTime = (580, 430, 720, 480)
# screen = ImageGrab.grab(s_checkTime)
# screen.show()
