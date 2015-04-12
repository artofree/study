# -*- coding: utf-8 -*-

print int("123"), int(12.34), str(123), bool(""), bool(-1), bool(0)

var1 = 21
var2 = "12"
print isinstance(var1, (int, float)), isinstance(var2, (int, str))

import math
#两个返回值情况
def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny

#据说是默认参数最大一个坑
def add_end(L=[]):
    L.append("end")
    return L
print add_end()
print add_end()

#可变参数
def calc(*numbers):
    count = 0
    for n in numbers:
        count = count + n
    return count
print calc(1, 2, 5)
print calc()

theNums =[1 ,2 ,3 ,4 ,5]
print calc(*theNums)

#函数变量
print "函数变量"

fun1 = abs
print fun1(-1)

def addFun(x ,y ,fun):
    return fun(x) +fun(y)
print addFun(3 ,-5 ,abs)

def squr(x):
    return x *x
print map(squr ,range(10))

print map(lambda x: x * x, [1, 2, 3, 4, 5, 6, 7, 8, 9])

def add(x ,y):
    return x +y
print reduce(add ,range(10))

def str2int(s):
    def fn(x, y):
        return x * 10 + y
    def char2num(s):
        return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
    return reduce(fn, map(char2num, s))
print str2int("12355")

#filter的处理函数返回bool值
def is_odd(n):
    return n % 2 == 1
print filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15])


print sorted(['bob', 'about', 'Zoo', 'Credit'])
def cmp_ignore_case(s1, s2):
    u1 = s1.upper()
    u2 = s2.upper()
    if u1 < u2:
        return -1
    if u1 > u2:
        return 1
    return 0
print sorted(['bob', 'about', 'Zoo', 'Credit'], cmp_ignore_case)






