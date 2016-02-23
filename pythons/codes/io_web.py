# -*- coding: utf-8 -*-

###url二进制文件读取
import urllib.request
# try:
#     thephoto = urllib.request.urlopen('').read()
# except:
#     continue
with codecs.open("1.jpg", 'wb') as f:
    f.write(thephoto)

###url文本文件：
import json
thePage =urllib.request.urlopen('').read().decode('utf8')
jsonResult =json.loads(thePage)

###文件读写
with open('C:\\topSeril\\1.txt', 'r') as f:
    theLines = f.readlines()
    for line in theLines:
        print(line.strip())  # 把末尾的'\n'删掉
import codecs
# windows的txt文件需要gbk解码
with codecs.open('d:\\guo', 'r', 'utf-8') as f:
    print(f.read())
#追加
with codecs.open('d:\\guo', 'a', 'utf-8') as f:
    f.write("好人郭鹏")

###目录操作
import os

print(os.name)
print(os.path.abspath("."))

# os.mkdir("d:\\newdir")


print([x for x in os.listdir('d:\\study\\pythons') if os.path.isfile(x) and os.path.splitext(x)[1] == '.py'])

theList = ["111", "222", "333", "444"]
with codecs.open('d:\\guo2', 'a', 'utf-8') as f:
    f.writelines(theList)

###检查是否有.py在某目录,且一次性情况用any和生成器
import os

if any(name.endswith('.py') for name in os.listdir('.')):
    print('There be python!')
