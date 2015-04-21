# -*- coding: utf-8 -*-
#resize用于各种变换
#thumbnail则只能用于等比例缩放
import os ,time ,codecs
from PIL import Image


photoPath =r'/Users/guopeng/Documents/panoramio/photos'
tiniPath =r'/Users/guopeng/Documents/panoramio/tinis'
smallPath =r'/Users/guopeng/Documents/panoramio/smalls'
tiniSize =(16 ,16)
smallSize =(64 ,64)

photoList =os.listdir(photoPath)
for thePhoto in photoList:
    if thePhoto.find('.jpg') >0:
        img =Image.open(os.path.join(photoPath ,thePhoto))
        out =img.resize(smallSize)
        out.save(os.path.join(smallPath ,thePhoto) ,'JPEG')
        out =img.resize(tiniSize)
        out.save(os.path.join(tiniPath ,thePhoto) ,'JPEG')




