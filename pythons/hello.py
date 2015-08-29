# -*- coding: utf-8 -*-
#in out
#print(r'\\\\t\\\')
print(r'\\\\t\\')

print("line1\nline2\nline3")
#等价于
print('''line1
line2
line3''')

print('Hi, %s, you have $%d.' % ('Michael', 1000000))

#变量
a = 'ABC'
b = a
a = 'XYZ'
print(b)

#只要x是非零数值、非空字符串、非空list等，就判断为True，否则为False
x = []
if x:
    print(True)

#is用于比较id，==用于比较值。此时None 1 为不变对象，指向同一个不变对象的变量id相同
#id相同值必然相同，值相同id未必相同
#None 没有==只有is or is not
l = None
if l is None:
    print(True)

var1 = 1
var2 = 1.0
if var1 is var2:
    print(1)
if var1 == var2:
    print(True)

#moudleZ
import sys

def test():
    args = sys.argv
    if len(args)==1:
        print('Hello, world!')
    elif len(args)==2:
        print('Hello, %s!' % args[1])
    else:
        print('Too many arguments!')

#一切可执行语句在被包含的时候就会被执行
#函数不会，__name__在命令行直接运行时为__main__，被包含时为hello
if __name__=='__main__':
    test()
else:
    print(__name__)

try:
    import io as StringIO
except ImportError: # 导入失败会捕获到ImportError
    import io

#__xxx__这样的变量是特殊变量，可以被直接引用，但是有特殊用途
#_xxx和__xxx这样的函数或变量就是非公开的

import sys
print(sys.path)

import os
print(os.getcwd())

print(os.path.dirname(os.path.dirname(__file__)))

import random
print(random.randint(0 ,10))


#zip用法：
l1 =[1 ,2 ,3 ,4 ,5]
l2 =['a' ,'b' ,'c' ,'d' ,'e']
print (list(zip(l1 ,l2)))
print (list(zip(*zip(l1 ,l2))))
matrix =[[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]
print (list(zip(*matrix)))
print (list(zip(*zip(*matrix))))

#
l1 =[n*n for n in range(10)]
print (l1)