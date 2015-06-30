# -*- coding: utf-8 -*-
# 从parser出的信息中选取测试文件

import os, urllib, threading, codecs, time, shutil

photoPath = r"E:\panoramio\allimages\1"
resultpath = r"/Users/guopeng/Documents/panoramio/1"

tList = []
dList = []

with codecs.open(resultpath, 'r', 'utf-8') as f:
    tList = [line.strip('\n') for line in f.readlines()]
resultList = [x.split('||') for x in tList]

for x in resultList:
    if len(x) < 16:
        dList.append(x)

#剩下的是数据齐全的干净图片
for x in dList:
    resultList.remove(x)

for x in resultList:
    for idx in range(-4, 0):
        if '|' in x[idx]:
            x[idx] = x[idx].strip('|')
        if x[idx] == '':
            x[idx] = '0'
        x[idx] = int(x[idx])

scoreList =[]
for x in resultList:
    scoreList.append(int(x[-1]) *6 +int(x[-2]) *10 +int(x[-3]) *8)
scoreList.sort(reverse=True)

score =scoreList[0]/15
for x in range(1,16):
    levelList =[]
    for idx in scoreList:
        if scoreList[idx] >score*(x-1) and scoreList[idx] <=score*x:
            levelList.append(idx)
    print len(levelList)

# 按-2，-3，-1排序
#resultList.sort(key=lambda x:(x[-2] ,x[-3] ,x[-1]) ,reverse=True)

#挪动到指定文件夹
# dList = resultList[:10000]
# for x in dList:
#     filename = x[0] + '.jpg'
#     srcPath = os.path.join(photoPath, filename)
#     tarPath = os.path.join(r'D:\panoramio\photos', filename)
#     shutil.copyfile(srcPath, tarPath)
