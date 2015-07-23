# -*- coding: utf-8 -*-

import os ,sys
try:
    import io as StringIO
except ImportError: # 导入失败会捕获到ImportError
    import io
from PIL import Image

outPath ='/Users/guopeng/Documents/panoramio/2028142.jpg'

oriPath ='/Users/guopeng/Documents/panoramio/smalls/2028142.jpg'
im =Image.open(oriPath)
print((im.mode()))
ios =io.StringIO()
print((ios.tell()))
im.save(ios ,'JPEG')
print((ios.tell()))

oriPath ='/Users/guopeng/Documents/panoramio/smalls/2028142.jpg'
im =Image.open(oriPath)
im.save(ios ,'JPEG')
print((ios.tell()))

ios.seek(1824)
cont =ios.read(1824)
with open(outPath, 'w') as f:
    f.write(cont)