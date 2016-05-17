__author__ = 'guo'
# -*- coding: utf-8 -*-

import cv2
import sys
import numpy as np
import os
import matplotlib.pyplot as plt

img =cv2.imread(r'/Users/guo/Desktop/digit_recognition/code/16-01/3.png', 0)
ret2,img = cv2.threshold(img,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
ret,img=cv2.threshold(img,127,1,cv2.THRESH_BINARY_INV)
#清空高度
avg =np.sum(img) /img.shape[0]
sum_x =np.sum(img ,axis=1)
del_list =[]
for x in range(img.shape[0]):
    if sum_x[x] <avg/2 or sum_x[x] >img.shape[1] -10:
        del_list.append(x)
img =np.delete(img ,del_list ,0)

#删直线
minLineLength = img.shape[0] -5
maxLineGap = 100
for x in range(180):
    lines = cv2.HoughLinesP(img,1,np.pi/(x +1),100,minLineLength,maxLineGap)
    if lines is not None:
        for x1,y1,x2,y2 in lines[0]:
            cv2.line(img,(x1,y1),(x2,y2),0,2)


img =255*img
cv2.imshow('image', img)
k = cv2.waitKey(0) &0xFF
if k == 27:
    cv2.destroyAllWindows()
