# -*- coding: utf-8 -*-

import os ,sys
from PIL import Image

oriPath = '/Users/guopeng/Documents/panoramio/smalls/2028142.jpg'
watermark = Image.new('RGBA', (256 ,256) ,(0 ,0 ,0 ,0))
im = Image.open(oriPath)
box = (100, 100, 164, 164)
region = im.crop(box)
watermark.paste(im ,(32 ,32 ,96 ,96))
watermark.save('/Users/guopeng/Documents/panoramio/test.png' ,'PNG')
i =0

# box = (100, 100, 400, 400)
# region = im.crop(box)
# im2 =Image.open(oriPath)
#
#
#
# print region.__class__
# print im.__class__