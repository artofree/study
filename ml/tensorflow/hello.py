__author__ = 'guo'
# -*- coding: utf-8 -*-

import tensorflow as tf

###最基本流程
# 创建一个常量 op, 产生一个 1x2 矩阵. 这个 op 被作为一个节点
# 加到默认图中. #
# 构造器的返回值代表该常量 op 的返回值.
matrix1 = tf.constant([[3., 3.]])
# 创建另外一个常量 op, 产生一个 2x1 矩阵.
matrix2 = tf.constant([[2.],[2.]])
# 创建一个矩阵乘法 matmul op , 把 'matrix1' 和 'matrix2' 作为输入. # 返回值 'product' 代表矩阵乘法的结果.
product = tf.matmul(matrix1, matrix2)
# 启动默认图.
# 调用 sess 的 'run()' 方法来执行矩阵乘法 op, 传入 'product' 作为该方法的参数.
# 上面提到, 'product' 代表了矩阵乘法 op 的输出, 传入它是向方法表明, 我们希望取回
# 矩阵乘法 op 的输出. #
# 整个执行过程是自动化的, 会话负责传递 op 所需的全部输入. op 通常是并发执行的. #
# 函数调用 'run(product)' 触发了图中三个 op (两个常量 op 和一个矩阵乘法 op) 的执行. #
# 返回值 'result' 是一个 numpy `ndarray` 对象.
with tf.Session() as sess:
  # result = sess.run([product ,matrix2])
  result =sess.run(product)
  print(result)

# ###变量的使用
# # Create a Variable, that will be initialized to the scalar value 0.
# state = tf.Variable(0, name="counter")
#
# # Create an Op to add one to `state`.
#
# one = tf.constant(1)
# new_value = tf.add(state, one)
# update = tf.assign(state, new_value)
#
# # 启动图后, 变量必须先经过`初始化` (init) op 初始化,
# # 首先必须增加一个`初始化` op 到图中.
# init_op = tf.initialize_all_variables()
#
# # Launch the graph and run the ops.
# with tf.Session() as sess:
#     # Run the 'init' op
#     #有变量就有这一句
#     sess.run(init_op)
#     # Print the initial value of 'state'
#     print(sess.run(state))
#     # Run the op that updates 'state' and print 'state'.
#     for _ in range(3):
#         print(_)
#         sess.run(update)
#         print(sess.run(state))
#         # print(state)