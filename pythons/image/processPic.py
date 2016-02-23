# -*- coding: utf-8 -*-
#resize用于各种变换
#thumbnail则只能用于等比例缩放
import os ,time ,codecs
from PIL import Image ,ImageDraw

def add_corners(im, rad):
    circle = Image.new('L', (rad * 2, rad * 2), 0)
    draw = ImageDraw.Draw(circle)
    draw.ellipse((0, 0, rad * 2, rad * 2), fill=255)
    alpha = Image.new('L', im.size, 255)
    w, h = im.size
    alpha.paste(circle.crop((0, 0, rad, rad)), (0, 0))
    alpha.paste(circle.crop((0, rad, rad, rad * 2)), (0, h - rad))
    alpha.paste(circle.crop((rad, 0, rad * 2, rad)), (w - rad, 0))
    alpha.paste(circle.crop((rad, rad, rad * 2, rad * 2)), (w - rad, h - rad))
    im.putalpha(alpha)
    return im


photoPath =r'/Users/guopeng/Documents/panoramio/photos'
tiniPath =r'/Users/guopeng/Documents/panoramio/tinis'
smallPath =r'/Users/guopeng/Documents/panoramio/smalls'
tiniSize =(12 ,12)
smallSize =(56 ,56)
bigsize =560
color =(192 ,192 ,192)
radius =40
distance =20

im =Image.open('/Users/guopeng/Documents/panoramio/blank.jpg')
photoList =os.listdir(photoPath)
for thePhoto in photoList:
    if thePhoto.find('.jpg') >0:
        im1 =Image.open(os.path.join(photoPath ,thePhoto))
        im1 =im1.resize((bigsize -2*distance,bigsize -2*distance),Image.ANTIALIAS)
        img =im1.resize((10,10),Image.ANTIALIAS)
        im1 =add_corners(im1 ,radius)
        im1.load()
        background = Image.new("RGB", im1.size, color)
        background.paste(im1, mask=im1.split()[3])

        #im2 =Image.new('RGBA', (bigsize,bigsize) ,color)
        im2 =im.resize((bigsize,bigsize),Image.ANTIALIAS)
        im2.paste(background,(distance ,distance ,bigsize-distance ,bigsize-distance))
        im2 =add_corners(im2 ,radius +distance)
        im2 =im2.resize(smallSize ,Image.ANTIALIAS)
        im2.save(os.path.join(smallPath ,thePhoto) ,'PNG' ,quality = 100)

        out = Image.new('RGBA', tiniSize ,(255,255,255))
        #out =im.resize(tiniSize,Image.ANTIALIAS)
        out.paste(img ,(1 ,1 ,11 ,11))
        out.save(os.path.join(tiniPath ,thePhoto) ,'JPEG' ,quality = 100)



#加框1
# photoList =os.listdir(photoPath)
# for thePhoto in photoList:
#     if thePhoto.find('.jpg') >0:
#         out = Image.new('RGBA', smallSize ,(127 ,127 ,127 ,1))
#         img =Image.open(os.path.join(photoPath ,thePhoto))
#         img =img.resize((54,54),Image.ANTIALIAS)
#         out.paste(img ,(1 ,1 ,55 ,55))
#         out.save(os.path.join(smallPath ,thePhoto) ,'JPEG' ,quality = 100)
#         out = Image.new('RGBA', tiniSize ,(127 ,127 ,127 ,1))
#         img =img.resize((14,14),Image.ANTIALIAS)
#         out.paste(img ,(1 ,1 ,15 ,15))
#         out.save(os.path.join(tiniPath ,thePhoto) ,'JPEG' ,quality = 100)






