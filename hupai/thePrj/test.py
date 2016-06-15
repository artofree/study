__author__ = 'guo'
# -*- coding: utf-8 -*-

import cv2
from PIL import ImageGrab ,Image
import numpy as np
import pyautogui,datetime,time ,threading


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
def test():
    return {'df' :1}

if test():
    print(1)


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
