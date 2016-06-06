__author__ = 'guo'
# -*- coding: utf-8 -*-

import cv2
import numpy as np
from matplotlib import pyplot as plt


img = cv2.imread(r'/Users/guo/Desktop/digit_recognition/code/16-01/5.png', 0)

# #cv2.CV_64F 􏰮出图像的深度􏰜数据类型􏰝􏰙可以使用-1, 与原图像保持一致
# laplacian=cv2.Laplacian(img,cv2.CV_64F)
# # 参数 1,0 为只在 x 方向求一􏲍导数􏰙最大可以求 2 􏲍导数。
# sobelx=cv2.Sobel(img,cv2.CV_64F,1,0,ksize=5)
# # 参数 0,1 为只在 y 方向求一􏲍导数􏰙最大可以求 2 􏲍导数。
# sobely=cv2.Sobel(img,cv2.CV_64F,0,1,ksize=5)
# plt.subplot(2,2,1),plt.imshow(img,cmap = 'gray')
# plt.title('Original'), plt.xticks([]), plt.yticks([])
# plt.subplot(2,2,2),plt.imshow(laplacian,cmap = 'gray')
# plt.title('Laplacian'), plt.xticks([]), plt.yticks([])
# plt.subplot(2,2,3),plt.imshow(sobelx,cmap = 'gray')
# plt.title('Sobel X'), plt.xticks([]), plt.yticks([])
# plt.subplot(2,2,4),plt.imshow(sobely,cmap = 'gray')
# plt.title('Sobel Y'), plt.xticks([]), plt.yticks([])
# plt.show()

sobelx8u = cv2.Sobel(img,cv2.CV_8U,1,0,ksize=5)
sobelx64f = cv2.Sobel(img,cv2.CV_64F,1,0,ksize=5)
abs_sobel64f = np.absolute(sobelx64f)
sobel_8u = np.uint8(abs_sobel64f)
plt.subplot(1,3,1),plt.imshow(img,cmap = 'gray')
plt.title('Original'), plt.xticks([]), plt.yticks([])
plt.subplot(1,3,2),plt.imshow(sobelx8u,cmap = 'gray')
plt.title('Sobel CV_8U'), plt.xticks([]), plt.yticks([])
plt.subplot(1,3,3),plt.imshow(sobel_8u,cmap = 'gray')
plt.title('Sobel abs(CV_64F)'), plt.xticks([]), plt.yticks([])
plt.show()
