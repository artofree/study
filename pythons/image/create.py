# -*- coding: utf-8 -*-

import os ,sys
from PIL import Image

oriPath = '/Users/guopeng/Documents/panoramio/photos/2028142.jpg'

im1 = Image.open(oriPath)
print im1.size[0]
box = (100, 100, 400, 400)
im2 = Image.open(oriPath)
im1.paste(im2 ,(0,0,im1.size[0] ,im1.size[1]))

# box = (100, 100, 400, 400)
# region = im.crop(box)
# im2 =Image.open(oriPath)
#
#
#
# print region.__class__
# print im.__class__