# -*- coding: utf-8 -*-
import time, threading

# 新线程执行的代码:
def loop():
    print('thread %s is running...' % threading.current_thread().name)
    n = 0
    while n < 5:
        n = n + 1
        print('thread %s >>> %s' % (threading.current_thread().name, n))
        time.sleep(1)
    print('thread %s ended.' % threading.current_thread().name)


def fun():
    print('thread %s is running...' % threading.current_thread().name)
    t = threading.Thread(target=loop, name='LoopThread')
    t2 = threading.Thread(target=loop, name='LoopThread2')
    t.start()
    t2.start()
    t2.join()
    t.join()
    print('thread %s ended.' % threading.current_thread().name)


def thread_fun(num):
    for n in range(0, int(num)):
        print(" I come from %s, num: %s" % ( threading.currentThread().getName(), n))
        time.sleep(1)

thread_list = list()
# 先创建线程对象
for i in range(0, 3):
    thread_name = "thread_%s" % i
    thread_list.append(threading.Thread(target=thread_fun, name=thread_name, args=(5,)))

# 启动所有线程
for thread in thread_list:
    thread.start()

# 主线程中等待所有子线程退出
for thread in thread_list:
    thread.join()