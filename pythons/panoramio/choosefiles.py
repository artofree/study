# -*- coding: utf-8 -*-
#从parser出的信息中选取测试文件

import os, urllib2, threading, codecs, time, shutil
from pyquery import PyQuery as pq
from lxml import etree

photoPath =r"E:\panoramio\allimages\1"
resultpath =r"E:\panoramio\parserresult\15"

tList =[]
dList =[]

with codecs.open(resultpath, 'r', 'utf-8') as f:
    tList =[line.strip('\n') for line in f.readlines()]
resultList =[x.split('||') for x in tList]

for x in resultList:
    if len(x) <15:
        dList.append(x)

for x in dList:
    resultList.remove(x)

for x in resultList:
    for idx in range(-3,0):
        x[idx] =int(x[idx])

#按-2，-3，-1排序
#resultList.sort(key=lambda x:(x[-2] ,x[-3] ,x[-1]) ,reverse=True)

#挪动到指定文件夹
dList =resultList[:10000]
for x in dList:
    filename =x[0] +'.jpg'
    srcPath =os.path.join(photoPath ,filename)
    tarPath =os.path.join(r'D:\panoramio\photos' ,filename)
    shutil.copyfile(srcPath ,tarPath)