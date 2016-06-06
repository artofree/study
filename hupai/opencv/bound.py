__author__ = 'guo'
# -*- coding: utf-8 -*-

import cv2

img = cv2.imread(r'/Users/guo/Desktop/digit_recognition/code/16-01/3.png', 0)
ret,thresh = cv2.threshold(img,127,255,0)
contours = cv2.findContours(thresh, 1, 2)
cnt = contours[0]
x,y,w,h = cv2.boundingRect(cnt)
img = cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)

cv2.imshow('image', img)
k = cv2.waitKey(0) &0xFF
if k == 27:
    cv2.destroyAllWindows()