__author__ = 'guo'
# -*- coding: utf-8 -*-

import tensorflow as tf
import numpy as np
import input_ as ip
import model as md

o_width =30
o_height =30


def train(init =1):
    x_data_set ,y_data_set=ip.load_new()

    x = tf.placeholder(tf.float32, [None ,28 ,28 ,1])
    y_ = tf.placeholder(tf.float32, shape=[None, 10])
    sess = tf.InteractiveSession()

    W_conv1 = md.weight_variable([5, 5, 1, 32])
    b_conv1 = md.bias_variable([32])
    h_conv1 = tf.nn.relu(md.conv2d(x, W_conv1) + b_conv1)
    h_pool1 = md.max_pool_2x2(h_conv1)
    W_conv2 = md.weight_variable([5, 5, 32, 64])
    b_conv2 = md.bias_variable([64])
    h_conv2 = tf.nn.relu(md.conv2d(h_pool1, W_conv2) + b_conv2)
    h_pool2 = md.max_pool_2x2(h_conv2)
    W_fc1 = md.weight_variable([7 * 7 * 64, 1024])
    b_fc1 = md.bias_variable([1024])
    h_pool2_flat = tf.reshape(h_pool2, [-1, 7 * 7 * 64])
    h_fc1 = tf.nn.relu(tf.matmul(h_pool2_flat, W_fc1) + b_fc1)
    keep_prob = tf.placeholder(tf.float32)
    h_fc1_drop = tf.nn.dropout(h_fc1, keep_prob)
    W_fc2 = md.weight_variable([1024, 10])
    b_fc2 = md.bias_variable([10])
    y_conv = tf.nn.softmax(tf.matmul(h_fc1_drop, W_fc2) + b_fc2)

    cross_entropy = tf.reduce_mean(-tf.reduce_sum(y_ * tf.log(y_conv), reduction_indices=[1]))
    train_step = tf.train.AdamOptimizer(1e-4).minimize(cross_entropy)
    correct_prediction = tf.equal(tf.argmax(y_conv, 1), tf.argmax(y_, 1))
    accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))

    saver = tf.train.Saver()
    if init:
        sess.run(tf.initialize_all_variables())
    else:
        saver.restore(sess, "param.ckpt")

    for i in range(1):
        ret =sess.run(train_step, feed_dict={x: ip.feed_x(), y_: ip.feed_y(), keep_prob: 0.5})

    saver.save(sess, "param.ckpt")
    print("test accuracy %g" % accuracy.eval(feed_dict={
        x: x_data_set, y_: y_data_set, keep_prob: 1.0}))


train(1)