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



















