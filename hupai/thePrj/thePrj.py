# -*- coding: utf-8 -*-

import cv2
from PIL import ImageGrab ,Image
import numpy as np
import pyautogui,datetime,time
import theLib.damatu as td

#初始化
pyautogui.click(x=600 ,y=865 ,button='left')
method = eval('cv2.TM_CCOEFF_NORMED')


while 1:
    # tmp =ImageGrab.grab((830 ,480 ,830 +300 ,480 +125))
    code_pic =ImageGrab.grab()
    code_pic =code_pic.crop((830 ,480 ,830 +300 ,480 +125))
    code_pic =cv2.cvtColor(np.array(code_pic, dtype=np.uint8), cv2.COLOR_RGBA2BGRA)





    cv2.imshow('image', code_pic)
    k = cv2.waitKey(0) &0xFF
    if k == 27:
        cv2.destroyAllWindows()
    time.sleep(3)

