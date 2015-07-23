# -*- coding: utf-8 -*-
print("100 + 200 =", 100+200)

#print r'\\\t\\\'
print(r'\\\\t\\')

print("line1\nline2\nline3")
#等价于
print('''line1
line2
line3''')

a = 100
if a > 0:
    print(a)
else:
    print(-a)

a = 'ABC'
b = a
a = 'XYZ'
print(b)

#print 'Hi, %s, you have $%d.'
print('Hi, %s, you have $%d.' % ('Michael', 1000000))

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

theList =[1]

def funs():
    i =len()

funs()
funs()
i =0











