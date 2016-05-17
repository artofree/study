import cv2
import numpy as np
import tensorflow as tf
from matplotlib import pyplot as plt

param =np.load('param.npz')
W_conv1 = tf.Variable(param['arr_0'])
b_conv1 = tf.Variable(param['arr_1'])
W_conv2 = tf.Variable(param['arr_2'])
b_conv2 = tf.Variable(param['arr_3'])
W_fc1 = tf.Variable(param['arr_4'])
b_fc1 = tf.Variable(param['arr_5'])
W_fc2 = tf.Variable(param['arr_6'])
b_fc2 = tf.Variable(param['arr_7'])
def conv2d(x, W):
    return tf.nn.conv2d(x, W, strides=[1, 1, 1, 1], padding='SAME')
def max_pool_2x2(x):
    return tf.nn.max_pool(x, ksize=[1, 2, 2, 1],
                          strides=[1, 2, 2, 1], padding='SAME')


img = cv2.imread(r'/Users/guo/Desktop/digit_recognition/code/16-01/3.png', 0)
# img = cv2.imread(r'/Users/guo/Desktop/841936.jpg', 0)
# global thresholding
ret2,img = cv2.threshold(img,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
ret,img=cv2.threshold(img,127,1,cv2.THRESH_BINARY_INV)
# print(img.shape)
# print(np.sum(img ,axis=1))

#清空y
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


testimg =img[:,0:40]


testimg =cv2.imread(r'/Users/guo/Desktop/digit_recognition/code/4.jpg', 0)
ret2,testimg = cv2.threshold(testimg,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
ret,testimg=cv2.threshold(testimg,127,1,cv2.THRESH_BINARY_INV)
testimg=cv2.resize(testimg,(28,28),interpolation=cv2.INTER_CUBIC)
sess = tf.InteractiveSession()
x_image =tf.Variable(initial_value=testimg ,dtype=tf.float32)
x_image1 = tf.reshape(x_image, [-1, 28, 28, 1])
h_conv1 = tf.nn.relu(conv2d(x_image1, W_conv1) + b_conv1)
h_pool1 = max_pool_2x2(h_conv1)
h_conv2 = tf.nn.relu(conv2d(h_pool1, W_conv2) + b_conv2)
h_pool2 = max_pool_2x2(h_conv2)
h_pool2_flat = tf.reshape(h_pool2, [-1, 7 * 7 * 64])
h_fc1 = tf.nn.relu(tf.matmul(h_pool2_flat, W_fc1) + b_fc1)
h_fc1_drop = tf.nn.dropout(h_fc1, 1.0)
y_conv = tf.nn.softmax(tf.matmul(h_fc1_drop, W_fc2) + b_fc2)
sess.run(tf.initialize_all_variables())
print(sess.run(y_conv))

testimg =255 *testimg
# img =127*img
cv2.imshow('image', testimg)
k = cv2.waitKey(0) &0xFF
if k == 27:
    cv2.destroyAllWindows()

















