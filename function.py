# -*- coding: utf-8 -*-

print int("123"), int(12.34), str(123), bool(""), bool(-1), bool(0)

var1 = 21
var2 = "12"
print isinstance(var1, (int, float)), isinstance(var2, (int, str))

fun1 = abs
print fun1(-1)

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



