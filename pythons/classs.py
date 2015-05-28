# -*- coding: utf-8 -*-
from copy import copy
import math

class mycls(object):
    def __init__(self ,val):
        self.val =val

mycls1 =mycls(1)
mycls2 =mycls1
mycls3 =copy(mycls1)

print(id(mycls1))
print(id(mycls2))
print(id(mycls3))

if mycls1 is mycls2:
    print(True)

if mycls1 ==mycls2:
    print(True)

if mycls2 ==mycls3:
    print(True)

mycls2.val =0

print(mycls1.val)
print(mycls3.val)


def genMatrix(rows,cols):
    matrix = [[str(col)+str(row) for col in range(cols)] for row in range(rows)]
    for i in range(rows):
        for j in range(cols):
            print(matrix[i][j], end=' ')
        print('\n')


genMatrix(3 ,5)
x1 =8.0
x2 =19.0
cellLen =(x2 -x1)/5

x3 =15.0
print(int(10.9999 / cellLen))


def fillSet(theSet):
    theList =[1 ,2 ,3]
    theSet.add(5)
    theSet.add(3)

    theSet -=set(theList)

myset =set()
fillSet(myset)
print(myset)

