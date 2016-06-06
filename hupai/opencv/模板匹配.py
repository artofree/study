__author__ = 'guo'
# -*- coding: utf-8 -*-

import cv2
from PIL import ImageGrab
import numpy as np
from matplotlib import pyplot as plt

img =ImageGrab.grab()
tmp =ImageGrab.grab((100 ,100 ,400 ,400))

cv2.imshow('image', img)
k = cv2.waitKey(0) &0xFF
if k == 27:
    cv2.destroyAllWindows()
elif k == ord('s'):
    cv2.imwrite('messigray.png', img)
    cv2.destroyAllWindows()
