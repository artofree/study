__author__ = 'guo'
# -*- coding: utf-8 -*-

import cv2
import numpy as np
from matplotlib import pyplot as plt


img = cv2.imread(r'/Users/guo/Desktop/digit_recognition/code/16-01/5.png', 0)

# global thresholding
ret1,th1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY) # Otsu's thresholding
ret2,th2 = cv2.threshold(img,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
blur = cv2.GaussianBlur(img,(5,5),0)
ret3,th3 = cv2.threshold(blur,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

cv2.imshow('image', th3)
k = cv2.waitKey(0) &0xFF
if k == 27:
    cv2.destroyAllWindows()

# # plot all the images and their histograms
# images = [img, 0, th1,
#           img, 0, th2,
#           blur, 0, th3]
# titles = ['Original Noisy Image','Histogram','Global Thresholding (v=127)',
#           'Original Noisy Image','Histogram',"Otsu's Thresholding",
#           'Gaussian filtered Image','Histogram',"Otsu's Thresholding"]
# #􏰰􏰀使用了 pyplot 中画直方图的方法?plt.hist, 􏰫注意的是它的参数是一维数组
# # 所以􏰰􏰀使用了􏰜numpy􏰝ravel 方法􏰙将多维数组􏰼换成一维􏰙也可以使用 flatten 方法 #ndarray.flat 1-D iterator over an array.
# #ndarray.flatten 1-D array copy of the elements of an array in row-major order.
# for i in range(3):
#     plt.subplot(3,3,i*3+1),plt.imshow(images[i*3],'gray')
#     plt.title(titles[i*3]), plt.xticks([]), plt.yticks([])
#     plt.subplot(3,3,i*3+2),plt.hist(images[i*3].ravel(),256)
#     plt.title(titles[i*3+1]), plt.xticks([]), plt.yticks([])
#     plt.subplot(3,3,i*3+3),plt.imshow(images[i*3+2],'gray')
#     plt.title(titles[i*3+2]), plt.xticks([]), plt.yticks([])
# plt.show()
