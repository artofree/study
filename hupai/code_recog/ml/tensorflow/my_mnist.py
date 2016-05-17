__author__ = 'guo'
# -*- coding: utf-8 -*-

import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data
import cv2

mnist = input_data.read_data_sets("MNIST_data/", one_hot=True)
x = tf.placeholder(tf.float32, [None, 784])
x_image = tf.reshape(x, [-1, 28, 28, 1])
x_image1 =tf.reshape(x, [-1, 28, 28])
W = tf.Variable(tf.zeros([784, 10]))
b = tf.Variable(tf.zeros([10]))
y = tf.nn.softmax(tf.matmul(x, W) + b)
y_ = tf.placeholder(tf.float32, [None, 10])
cross_entropy = tf.reduce_mean(-tf.reduce_sum(y_ * tf.log(y), reduction_indices=[1]))
train_step = tf.train.GradientDescentOptimizer(0.5).minimize(cross_entropy)

init = tf.initialize_all_variables()
sess = tf.Session()
sess.run(init)
for i in range(1000):
    img_x ,img_y =mnist.train.next_batch(1)
    # img =sess.run(x_image, feed_dict={x: img_x})
    img =sess.run(x_image1, feed_dict={x: img_x})

    cv2.imshow('image', img[0])
    k = cv2.waitKey(0) &0xFF
    if k == 27:
        cv2.destroyAllWindows()

    batch_xs, batch_ys = mnist.train.next_batch(100)
    sess.run(train_step, feed_dict={x: batch_xs, y_: batch_ys})
    ret =sess.run([train_step ,cross_entropy ,W ,b ,y], feed_dict={x: batch_xs, y_: batch_ys})
    print(ret[2])
    rrr =100
    # print(sess.run([train_step ,cross_entropy ,W ,b ,y], feed_dict={x: batch_xs, y_: batch_ys}))
    # print(cross_entropy)

correct_prediction = tf.equal(tf.argmax(y, 1), tf.argmax(y_, 1))
accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))
print(sess.run(accuracy, feed_dict={x: mnist.test.images, y_: mnist.test.labels}))
