# -*- coding: utf-8 -*-

import math

class ltlnrect(object):
    def __init__(self, nelt, swlt ,neln ,swln):
        self.nelt = nelt
        self.neln = neln
        self.swlt = swlt
        self.swln = swln
        self.ct =(nelt +swlt)/2
        self.cn =(neln +swln)/2

    #按相限来
    def pointIndex(self ,lt ,ln):
        if self.nelt >=lt >self.ct:
            if self.neln >=ln >self.cn:
                return 0
            elif self.cn >=ln >self.swln:
                return 1
            else:
                return -1
        elif self.ct >=lt >self.swlt:
            if self.neln >=ln >self.cn:
                return 3
            elif self.cn >=ln >self.swln:
                return 2
            else:
                return -1
        else:
            return -1

    def indexRect(self ,index):
        if index ==0:
            rect =ltlnrect(self.nelt ,self.ct ,self.neln ,self.cn)
            return rect
        elif index ==1:
            rect =ltlnrect(self.nelt ,self.ct ,self.cn ,self.swln)
            return rect
        elif index ==3:
            rect =ltlnrect(self.ct ,self.swlt ,self.neln ,self.cn)
            return rect
        else:
            rect =ltlnrect(self.ct ,self.swlt ,self.cn ,self.swln)
            return rect

theRect =ltlnrect(90.0 ,-90.0 ,180.0 ,-180.0)
theCount =int(math.pow(2 ,8))
print(type(theCount))
ltLen =(theRect.nelt -theRect.swlt)/theCount
lnLen =(theRect.neln -theRect.swln)/theCount
matrix = [[ltlnrect(theRect.nelt -col*ltLen ,theRect.nelt -(col +1)*ltLen ,theRect.swln +(row +1)*lnLen ,theRect.swln +row *lnLen) for col in range(theCount)] for row in range(theCount)]
c1 =matrix[0][0]
c2 =matrix[0][1]
c3 =matrix[1][0]
c4 =matrix[1][1]
lt =-33.0
ln =78.0
c =matrix[int((ln -theRect.swln)/lnLen)][int((theRect.nelt -lt)/ltLen)]
i =0