# -*- coding: utf-8 -*-

l1 =[1 ,2 ,3 ,4 ,5]
l2 =['a' ,'b' ,'c' ,'d' ,'e']

l3 =[x *y for x in l1 for y in l1]
print(l3)