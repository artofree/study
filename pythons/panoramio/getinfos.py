# -*- coding: utf-8 -*-
#抓取所有已下载图片的状态信息，保存全部状态信息，同时抽取整合所有基本信息
#整合信息包括：photoid,userid,lt,ln,
import os, urllib.request, urllib.error, urllib.parse, threading, codecs, time

def dlstatus(threadid):
    photoPath =os.path.join('E:\\panoramio\\allimages'  ,str(threadid))
    statusPath =os.path.join('E:\\panoramio\\allinfos'  ,str(threadid))
    photoList =[os.path.splitext(x)[0] for x in os.listdir(photoPath)]
    print('thread ' +str(threadid) +' is ' +str(len(photoList)))
    statusList =[os.path.splitext(x)[0] for x in os.listdir(statusPath)]
    statusSet =set(statusList)
    print('thread ' +str(threadid) +' is ' +str(len(statusList)))
    print('thread ' +str(threadid) +' is ' +str(len(statusSet)))
    for thePhoto in photoList:
        if thePhoto not in statusSet:
            theUrl =r'http://www.panoramio.com/photo/' +thePhoto
            try:
                thePage  =urllib.request.urlopen(theUrl).read()
            except:
                continue
            with codecs.open(os.path.join(statusPath  ,thePhoto) +".htm", 'wb') as f:
                f.write(thePage)
            statusSet.add(thePhoto)

    print('thread ' +str(threadid) +' is finished!')

threads =[]
threads.append(threading.Thread(target=dlstatus ,name="thread3" ,args=(3,)))

for t in threads:
    t.start()
    time.sleep(10)
for t in threads:
    t.join()

print("congratulation!")
