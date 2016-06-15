__author__ = 'guo'
# -*- coding: utf-8 -*-

import cv2
from PIL import ImageGrab ,Image
import numpy as np
import datetime

print(datetime.datetime.now())
img =ImageGrab.grab()
print(datetime.datetime.now())
tmp =ImageGrab.grab((100 ,100 ,400 ,400))
print(datetime.datetime.now())
# img =np.array(img, dtype=np.uint8)
# tmp =np.array(tmp, dtype=np.uint8)
img =cv2.cvtColor(np.array(img, dtype=np.uint8), cv2.COLOR_RGB2GRAY)
tmp =cv2.cvtColor(np.array(tmp, dtype=np.uint8), cv2.COLOR_RGB2GRAY)
# img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# tmp = cv2.cvtColor(tmp,cv2.COLOR_BGR2GRAY)
print(datetime.datetime.now())
cv2.imshow('image', tmp)
k = cv2.waitKey(0) &0xFF
if k == 27:
    cv2.destroyAllWindows()
w, h = 300 ,300
print(datetime.datetime.now())
method = eval('cv2.TM_CCOEFF_NORMED')
res = cv2.matchTemplate(img,tmp,method)
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
print(datetime.datetime.now())
print(max_loc)

# cv2.imshow('image', img)
# k = cv2.waitKey(0) &0xFF
# if k == 27:
#     cv2.destroyAllWindows()
# elif k == ord('s'):
#     cv2.imwrite('messigray.png', img)
#     cv2.destroyAllWindows()
