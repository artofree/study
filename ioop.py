# -*- coding: utf-8 -*-

with open('C:\\topSeril\\1.txt', 'r') as f:
    theLines =f.readlines()
    for line in theLines:
        print line.strip() # 把末尾的'\n'删掉

import codecs
#windows的txt文件需要gbk解码
with codecs.open('d:\\guo', 'r', 'utf-8') as f:
    print f.read()

with codecs.open('d:\\guo', 'a', 'utf-8') as f:
    f.write(u"好人郭鹏")

import os
print os.name
print os.path.abspath(".")

#os.mkdir("d:\\newdir")


print [x for x in os.listdir('d:\\study') if os.path.isfile(x) and os.path.splitext(x)[1] =='.py']

theList =["111" ,"222" ,"333" ,"444"]
with codecs.open('d:\\guo', 'a', 'utf-8') as f:
    f.writelines(theList)









