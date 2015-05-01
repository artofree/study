# -*- coding: utf-8 -*-

import os ,sys
from PIL import Image

oriPath = 'C:\\Users\\peng\\Desktop\\123.jpg'

im = Image.open(oriPath)
box = (100, 100, 400, 400)
region = im.crop(box)
print region
print type(im.size())
# box = (100, 100, 400, 400)
# region = im.crop(box)
# im2 =Image.open(oriPath)
#
#
#
# print region.__class__
# print im.__class__