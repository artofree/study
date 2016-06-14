__author__ = 'guo'
# -*- coding: utf-8 -*-

import cv2
from PIL import ImageGrab ,Image
import numpy as np
import datetime

img =ImageGrab.grab()
tmp =ImageGrab.grab((100 ,100 ,400 ,400))
img =np.array(img, dtype=np.uint8)
tmp =np.array(tmp, dtype=np.uint8)
w, h = 300 ,300
d1 =datetime.datetime.now()
method = eval('cv2.TM_CCOEFF_NORMED')
res = cv2.matchTemplate(img,tmp,method)
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
d2 =datetime.datetime.now()
print((d2 -d1).microseconds)
print(max_loc)

# cv2.imshow('image', img)
# k = cv2.waitKey(0) &0xFF
# if k == 27:
#     cv2.destroyAllWindows()
# elif k == ord('s'):
#     cv2.imwrite('messigray.png', img)
#     cv2.destroyAllWindows()
