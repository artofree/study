# -*- coding: utf-8 -*-

import os ,codecs

photoList =[os.path.splitext(x)[0] for x in os.listdir('/Users/guo/Documents/panoramio/photos') if os.path.splitext(x)[1] =='.jpg']
with codecs.open('/Users/guo/Documents/1') as f:
    resultList =[line.strip().split('||')[0] for line in f.readlines()]
for photo in photoList:
    if photo in resultList:
        print (photo)
i =0