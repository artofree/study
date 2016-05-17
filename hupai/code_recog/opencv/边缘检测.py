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

img =th2
edges = cv2.Canny(img,100,200)
plt.subplot(121),plt.imshow(img,cmap = 'gray')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(edges,cmap = 'gray')
plt.title('Edge Image'), plt.xticks([]), plt.yticks([])
plt.show()
