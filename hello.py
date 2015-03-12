# -*- coding: utf-8 -*-
print "100 + 200 =", 100+200

#print r'\\\t\\\'
print r'\\\\t\\'

print "line1\nline2\nline3"
#等价于
print '''line1
line2
line3'''

a = 100
if a > 0:
    print a
else:
    print -a

a = 'ABC'
b = a
a = 'XYZ'
print b

print 'Hi, %s, you have $%d.' % ('Michael', 1000000)

#is用于比较id，==用于比较值。此时None 1 为不变对象，指向同一个不变对象的变量id相同
#id相同值必然相同，值相同id未必相同
l = None
if l is None:
    print True

var1 = 1
var2 = 1.0
if var1 is var2:
    print 1
if var1 == var2:
    print True





















