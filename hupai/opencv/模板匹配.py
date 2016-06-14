__author__ = 'guo'
# -*- coding: utf-8 -*-

import cv2
from PIL import ImageGrab ,Image
import numpy as np
from matplotlib import pyplot as plt

img =ImageGrab.grab()
tmp =ImageGrab.grab((100 ,100 ,400 ,400))
img =np.array(img, dtype=np.uint8)
tmp =np.array(tmp, dtype=np.uint8)
w, h = 300 ,300
method = eval('cv2.TM_CCOEFF')
res = cv2.matchTemplate(img,tmp,method)
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

cv2.imshow('image', img)
k = cv2.waitKey(0) &0xFF
if k == 27:
    cv2.destroyAllWindows()
elif k == ord('s'):
    cv2.imwrite('messigray.png', img)
    cv2.destroyAllWindows()
