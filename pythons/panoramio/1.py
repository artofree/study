# -*- coding: utf-8 -*-
#将所有fullimage的paser信息和对应1920图片整理出来

import os, urllib.request, urllib.parse, urllib.error, threading, codecs, time, shutil

photourl =r"E:\panoramio\fullImages"
sourceurl =r"E:\panoramio\allimages"
parserurl =r"E:\panoramio\parserresult\16"
desurl =r"E:\samples"


#shutil.copy(os.path.join(parserurl ,os.listdir(parserurl)[0]) ,"E:\\samples")

sourceList =[]
for x in range(1 ,11):
    sourceList.append(os.listdir(os.path.join(sourceurl ,str(x))))

parserDict =dict()
for x in range(1 ,11):
    with codecs.open(os.path.join(parserurl ,str(x)), 'r', 'utf-8') as f:
        for line in f.readlines():
            parserDict[line[:line.find("||")]] =line

parserList =[]
for index in range(1 ,11):
    photoList =os.listdir(os.path.join(photourl ,str(index)))
    for photo in photoList:
        photoid =os.path.splitext(photo)[0]
        if photoid in parserDict:
            parserList.append(parserDict[photoid])
        for idx in range(10):
            if photo in sourceList[idx]:
                shutil.copy(os.path.join(os.path.join(sourceurl ,str(idx +1)) ,photo) ,os.path.join(desurl ,str(index)))
                break
with codecs.open(os.path.join(desurl ,"parser"), 'a', 'utf-8') as f:
    f.writelines(parserList)
