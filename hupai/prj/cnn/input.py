import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data
import numpy as np
import scipy.io as sio
import cv2




def load_old():
    pass


def load_new():
    load_data = sio.loadmat('/Users/guo/Downloads/DigitRecognition-master/src/newX.mat')
    x = load_data['X']
    x = x.reshape(2644, 30, 30)
    for index in range(x.shape[0]):
        x[index] = x[index].T
    x = x[:, 1:-1, 1:-1]
    x = x.reshape(2644, 784)
    load_data = sio.loadmat('/Users/guo/Downloads/DigitRecognition-master/src/newy.mat')
    y = load_data['y']
    y = y.T
    y_ = np.zeros((2644, 10))
    y_[np.arange(2644), y] = 1
    return x, y_


def feed_x():
    load_data = sio.loadmat('/Users/guo/Downloads/DigitRecognition-master/src/newX.mat')
    sess = tf.Session()
    x = load_data['X']
    x = x.reshape(2644, 30, 30)
    for index in range(x.shape[0]):
        x[index] = x[index].T
    x = x.reshape(2644, 30, 30 ,1)
    x_ =np.zeros([2644 ,28 ,28 ,1])
    img_input = tf.placeholder(tf.float32, [30 ,30 ,1])
    img_crop= tf.random_crop(img_input, [28, 28, 1])
    # img_lr = tf.image.random_flip_left_right(img_crop)
    # img_ud = tf.image.random_flip_up_down(img_lr)
    # img_b = tf.image.random_brightness(img_crop, max_delta=63)
    # img_c = tf.image.random_contrast(img_crop, lower=0.2, upper=1.8)
    img_w = tf.image.per_image_whitening(img_crop)
    init = tf.initialize_all_variables()
    sess.run(init)
    for index in range(x.shape[0]):
        img =sess.run(img_w ,feed_dict={img_input: x[index]})
        cv2.imshow('image', img)
        k = cv2.waitKey(0) &0xFF
        if k == 27:
            cv2.destroyAllWindows()
        x_[index] =img
    sess.close()
    return x_

def feed_y():
    load_data = sio.loadmat('/Users/guo/Downloads/DigitRecognition-master/src/newy.mat')
    y = load_data['y']
    y = y.T
    y_ = np.zeros((2644, 10))
    y_[np.arange(2644), y] = 1
    return y_
