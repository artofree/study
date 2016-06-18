__author__ = 'guo'
# -*- coding: utf-8 -*-

import cv2
from PIL import ImageGrab ,Image
import numpy as np
import pyautogui,datetime,time ,threading ,win32api

method = eval('cv2.TM_CCOEFF_NORMED')
begin_x =800
begin_y =100
timeTarget =Image.open(r'C:\Users\guo\Desktop\thePrj\alltobid\29_3.png')
timeTarget =cv2.cvtColor(np.array(timeTarget, dtype=np.uint8), cv2.COLOR_RGBA2GRAY)
timeStamp =0
theCodeDict ={}
lock = threading.Lock()
code_url =r'C:\Users\guo\Desktop\thePrj\alltobid\code.png'

# def fun():
#     global timeTarget
#     global timeStamp
#     screen =ImageGrab.grab((500 ,200 ,900 ,600))
#     screen =cv2.cvtColor(np.array(screen, dtype=np.uint8), cv2.COLOR_RGB2GRAY)
#     res = cv2.matchTemplate(screen,timeTarget,method)
#     min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
#     if max_val >0.99:
#         timeStamp =3



################################################################################################################
def check_img(url):
    target =Image.open(url)
    target =cv2.cvtColor(np.array(target, dtype=np.uint8), cv2.COLOR_RGBA2GRAY)
    screen =ImageGrab.grab((begin_x ,begin_y ,1400 ,800))
    screen =cv2.cvtColor(np.array(screen, dtype=np.uint8), cv2.COLOR_RGB2GRAY)
    res = cv2.matchTemplate(screen,target,method)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    if max_val >0.9:
        return max_loc
    else:
        return 0

def fun():
    target =Image.open(r'C:\Users\guo\Desktop\thePrj\alltobid\tip_end.png')
    tip_loc =check_img(r'C:\Users\guo\Desktop\thePrj\alltobid\tip_begin.png')
    left ,top=begin_x +tip_loc[0] ,begin_y +tip_loc[1]
    tip_loc =check_img(r'C:\Users\guo\Desktop\thePrj\alltobid\tip_end.png')
    right ,bottom =begin_x +tip_loc[0] +target.width ,begin_y +tip_loc[1] +target.height
    tip =ImageGrab.grab((left ,top ,right ,bottom))
    tip =tip.resize((tip.width *2,90))
    code =ImageGrab.grab((1000 ,450 ,1000 +150 ,450 +90))
    code =code.resize((code.width *2 ,code.height *2) ,Image.ANTIALIAS)
    ret =Image.new('RGB', (tip.width +code.width, code.height), (255, 255, 255))
    # ret =Image.new('L', (tip.width +code.width, code.height), 255)
    ret.paste(tip ,(0 ,(ret.height -tip.height) //2 ,tip.width ,(ret.height -tip.height) //2 +tip.height))
    ret.paste(code ,(tip.width,0,ret.width,ret.height))
    ret.save(code_url, "PNG")

pyautogui.click(x=260 ,y=1060 ,button='left')
fun()
#######################################################################################
# time_tuple = (2012, # Year
#                  9, # Month
#                  6, # Day
#                  0, # Hour
#                 38, # Minute
#                  0, # Second
#                  0, # Millisecond
#               )
# dayOfWeek = datetime.datetime(2012,9,6,0,38,0,0).isocalendar()[2]
# win32api.SetSystemTime(2012,9 ,dayOfWeek ,6,0,38,0,0)

# target =Image.open(r'C:\Users\guo\Desktop\thePrj\51\refresh_code_button.png')
# target =cv2.cvtColor(np.array(target, dtype=np.uint8), cv2.COLOR_RGBA2GRAY)
# screen =Image.open(r'C:\Users\guo\Pictures\Screenshots\1.png')
# screen =cv2.cvtColor(np.array(screen, dtype=np.uint8), cv2.COLOR_RGBA2GRAY)
# method = eval('cv2.TM_CCOEFF_NORMED')
# res = cv2.matchTemplate(screen,target,method)
# min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
# i =0


# pyautogui.click(x=260 ,y=1060 ,button='left')
# target =Image.open(r'C:\Users\guo\Desktop\thePrj\51\test.png')
# target =cv2.cvtColor(np.array(target, dtype=np.uint8), cv2.COLOR_RGBA2GRAY)
# screen =ImageGrab.grab((800 ,100 ,1400 ,800))
# screen =cv2.cvtColor(np.array(screen, dtype=np.uint8), cv2.COLOR_RGB2GRAY)
# method = eval('cv2.TM_CCOEFF_NORMED')
# res = cv2.matchTemplate(screen,target,method)
# min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
# tmp =ImageGrab.grab((800 +max_loc[0] ,100 +max_loc[1] ,1920 ,1080))
# tmp.show()


# d1 =datetime.datetime.now()
# method = eval('cv2.TM_CCOEFF_NORMED')
# target =Image.open(r"C:\Users\guo\Desktop\thePrj\51\confirm_code_button.png")
# target =cv2.cvtColor(np.array(target, dtype=np.uint8), cv2.COLOR_RGBA2BGR)
# screen =Image.open(r"C:\Users\guo\Pictures\Screenshots\1.png")
# screen =cv2.cvtColor(np.array(screen, dtype=np.uint8), cv2.COLOR_RGBA2BGR)
# res = cv2.matchTemplate(screen,target,method)
# min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
# d2 =datetime.datetime.now()
# print((d2 -d1).microseconds)
# print(max_loc)

# cv2.imshow('image', img)
# k = cv2.waitKey(0) &0xFF
# if k == 27:
#     cv2.destroyAllWindows()
# elif k == ord('s'):
#     cv2.imwrite('messigray.png', img)
#     cv2.destroyAllWindows()
