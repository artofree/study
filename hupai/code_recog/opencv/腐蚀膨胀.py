__author__ = 'guo'
# -*- coding: utf-8 -*-

import cv2
import numpy as np
from matplotlib import pyplot as plt


img = cv2.imread(r'/Users/guo/Desktop/digit_recognition/code/16-01/3.png', 0)

ret1,th1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY) # Otsu's thresholding
ret2,th2 = cv2.threshold(img,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
blur = cv2.GaussianBlur(img,(5,5),0)
ret3,th3 = cv2.threshold(blur,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

kernel = np.ones((5,5),np.uint8)
erosion = cv2.erode(th3,kernel,iterations = 1)
dilation = cv2.dilate(erosion,kernel,iterations = 1)

cv2.imshow('image', dilation)

k = cv2.waitKey(0) &0xFF
if k == 27:
    cv2.destroyAllWindows()
