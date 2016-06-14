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
    x = load_data['X']
    x = x.reshape(2644, 30, 30)
    x = x[:, 1:-1, 1:-1]
    for index in range(x.shape[0]):
        x[index] = x[index].T


def feed_y():
    load_data = sio.loadmat('/Users/guo/Downloads/DigitRecognition-master/src/newy.mat')
    y = load_data['y']
    y = y.T
    y_ = np.zeros((2644, 10))
    y_[np.arange(2644), y] = 1
    return y_
