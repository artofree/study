__author__ = 'guo'
# -*- coding: utf-8 -*-

import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data
import numpy as np
import scipy.io as sio
import cv2

# load_data = sio.loadmat('/Users/guo/Downloads/DigitRecognition-master/src/newX.mat')
# arr = load_data['X']
# print(arr.shape)
#
# a =np.array([[6, 7, 1, 6],
#        [1, 0, 2, 3],
#        [7, 8, 2, 1]])
# a =np.reshape(a ,[3 ,4 ,1])
# print(a)
#
# print(a[1])
# np.savez('param.npz' ,a)

# index = 0
# if index:
#     a = 1
# else:
#     a = 0
#
# print(a)
#
# print([x for x in range(10)])
#
# a = np.array([1, 0, 3])
# b = np.zeros((3, 4))
# b[np.arange(3), a] = 1
# print(b)
img =np.ones([100 ,100])

img = cv2.imread(r'/Users/guo/Desktop/digit_recognition/code/16-01/3.png', 0)
ret2,img = cv2.threshold(img,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
img =img +1
img =img.astype(float)

cv2.imshow('image', img)
k = cv2.waitKey(0) &0xFF
if k == 27:
    cv2.destroyAllWindows()
