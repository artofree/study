# -*- coding: utf-8 -*-
#用于把目录下所有文件内容set并集中起来

import os, codecs

fileList =os.listdir("e:\\panoramio\\x90y45_16\\")
fileList.sort()
photoSet =set()
#photoSet =[]
print type(photoSet)
for fileUrl in fileList:
    with codecs.open("e:\\panoramio\\x90y45_16\\" +fileUrl, 'r', 'utf-8') as f:
        photoSet |=set(f.readlines())
#        photoSet +=f.readlines()

print len(photoSet)
with codecs.open("e:\\panoramio\\x90y45_16\\panoramio", 'w', 'utf-8') as f:
    f.writelines(photoSet)