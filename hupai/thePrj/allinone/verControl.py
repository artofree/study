import damatu as td
import myLib ,damatu
from PIL import ImageGrab, Image
import numpy as np
import cv2 ,pyautogui, datetime, time, threading, requests
from io import BytesIO as StringIO
import configparser ,json ,zipfile ,os

servUrl ='http://139.219.238.37:8000/'
fileUrl =r"C:\Users\guo\Desktop\archive.zip"

myLib.zipDir(r".", r"C:\Users\guo\Desktop\archive.zip")
files = {'file': open(fileUrl, 'rb')}
r = requests.post(servUrl +'setVersionContent', files=files)