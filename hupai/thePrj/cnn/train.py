__author__ = 'guo'
# -*- coding: utf-8 -*-

import tensorflow as tf
import numpy as np
import input as ip
import model as md


def train(param =0 ,dataurl =0):
    if dataurl:
        x_data_set ,y_data_set=ip.load_new()
    else:
        x_data_set ,y_data_set =ip.load_old()

    if param:
        W_conv1,b_conv1,W_conv2,b_conv2,W_fc1,b_fc1,W_fc2,b_fc2 =md.load_param()
    else:
        W_conv1,b_conv1,W_conv2,b_conv2,W_fc1,b_fc1,W_fc2,b_fc2 =md.create_param()

    x = tf.placeholder(tf.float32, [None, 784])
    y_ = tf.placeholder(tf.float32, shape=[None, 10])
    x_image = tf.reshape(x, [-1, 28, 28, 1])
    sess = tf.InteractiveSession()
    h_conv1 = tf.nn.relu(md.conv2d(x_image, W_conv1) + b_conv1)
    h_pool1 = md.max_pool_2x2(h_conv1)
    h_conv2 = tf.nn.relu(md.conv2d(h_pool1, W_conv2) + b_conv2)
    h_pool2 = md.max_pool_2x2(h_conv2)
    h_pool2_flat = tf.reshape(h_pool2, [-1, 7 * 7 * 64])
    h_fc1 = tf.nn.relu(tf.matmul(h_pool2_flat, W_fc1) + b_fc1)
    keep_prob = tf.placeholder(tf.float32)
    h_fc1_drop = tf.nn.dropout(h_fc1, keep_prob)
    y_conv = tf.nn.softmax(tf.matmul(h_fc1_drop, W_fc2) + b_fc2)
    cross_entropy = tf.reduce_mean(-tf.reduce_sum(y_ * tf.log(y_conv), reduction_indices=[1]))
    train_step = tf.train.AdamOptimizer(1e-4).minimize(cross_entropy)
    correct_prediction = tf.equal(tf.argmax(y_conv, 1), tf.argmax(y_, 1))
    accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))
    sess.run(tf.initialize_all_variables())

    for i in range(10):
        # train_step.run(feed_dict={x: [x_data_set[i]], y_: [y_data_set[i]], keep_prob: 0.5})
        ret =sess.run([train_step ,x_image], feed_dict={x: [x_data_set[i]], y_: [y_data_set[i]], keep_prob: 0.5})
        if i +1 ==x_data_set.shape[0]:
            ret =sess.run([train_step ,W_conv1 ,b_conv1 ,W_conv2 ,b_conv2 ,W_fc1 ,b_fc1 ,W_fc2 ,b_fc2] ,feed_dict={x: [x_data_set[i]], y_: [y_data_set[i]], keep_prob: 0.5})
            np.savez('param.npz' ,ret[1] ,ret[2] ,ret[3] ,ret[4] ,ret[5] ,ret[6] ,ret[7] ,ret[8])

    print("test accuracy %g" % accuracy.eval(feed_dict={
        x: x_data_set, y_: y_data_set, keep_prob: 1.0}))


train(0 ,1)