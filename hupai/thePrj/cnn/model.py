import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data
import numpy as np
import scipy.io as sio
import cv2

def weight_variable(shape):
    initial = tf.truncated_normal(shape, stddev=0.1)
    return tf.Variable(initial)


def bias_variable(shape):
    initial = tf.constant(0.1, shape=shape)
    return tf.Variable(initial)


def conv2d(x, W):
    return tf.nn.conv2d(x, W, strides=[1, 1, 1, 1], padding='SAME')


def max_pool_2x2(x):
    return tf.nn.max_pool(x, ksize=[1, 2, 2, 1],
                          strides=[1, 2, 2, 1], padding='SAME')

def load_param():
    param =np.load('param.npz')
    W_conv1 = tf.Variable(param['arr_0'])
    b_conv1 = tf.Variable(param['arr_1'])
    W_conv2 = tf.Variable(param['arr_2'])
    b_conv2 = tf.Variable(param['arr_3'])
    W_fc1 = tf.Variable(param['arr_4'])
    b_fc1 = tf.Variable(param['arr_5'])
    W_fc2 = tf.Variable(param['arr_6'])
    b_fc2 = tf.Variable(param['arr_7'])
    return W_conv1,b_conv1,W_conv2,b_conv2,W_fc1,b_fc1,W_fc2,b_fc2

def create_param():
    W_conv1 = weight_variable([5, 5, 1, 32])
    b_conv1 = bias_variable([32])
    W_conv2 = weight_variable([5, 5, 32, 64])
    b_conv2 = bias_variable([64])
    W_fc1 = weight_variable([7 * 7 * 64, 1024])
    b_fc1 = bias_variable([1024])
    W_fc2 = weight_variable([1024, 10])
    b_fc2 = bias_variable([10])
    return W_conv1,b_conv1,W_conv2,b_conv2,W_fc1,b_fc1,W_fc2,b_fc2




# img =cv2.imread(r'/Users/guo/Desktop/digit_recognition/code/2.jpg', 0)
# imgs =np.array([img ,img ,img])
# print(imgs.shape)
# x_image = tf.reshape(imgs, [3 ,100, 100, 1])
# img_crop= tf.random_crop(x_image, [64, 64, 1])
# sess = tf.InteractiveSession()
# sess.run(tf.initialize_all_variables())
# img =sess.run(img_crop)
#
# # img =127*img
# cv2.imshow('image', img[1])
# k = cv2.waitKey(0) &0xFF
# if k == 27:
#     cv2.destroyAllWindows()