# -*- coding: utf-8 -*-
import os, urllib2, threading, codecs

def dlimages(threadid ,index):
    photolist =[]
    photourl ="E:\\allimages\\" +str(threadid) +"\\"
    with codecs.open("d:\\panoramio\\panoramio", 'r', 'utf-8') as f:
        if threadid ==10:
            photolist =f.readlines()[170000 *(threadid -1) +index:]
        else:
            photolist =f.readlines()[170000 *(threadid -1) +index:170000 *threadid]

    for photo in photolist:
        weburl =r"http://static.panoramio.com/photos/1920x1280/" +photo.strip() +r".jpg"
        try:
            thephoto  =urllib2.urlopen(weburl).read()
        except:
            continue
        with codecs.open(photourl +photo.strip() +".jpg", 'wb') as f:
            f.write(thephoto)
        index +=1
        with codecs.open("E:\\allimages\\_" +str(threadid), 'w', 'utf-8') as f:
            f.writelines(str(index))


threads =[]
threads.append(threading.Thread(target=dlimages ,name="thread1" ,args=(1,291)))
threads.append(threading.Thread(target=dlimages ,name="thread2" ,args=(2,216)))
threads.append(threading.Thread(target=dlimages ,name="thread3" ,args=(3,20)))
threads.append(threading.Thread(target=dlimages ,name="thread4" ,args=(4,199)))
threads.append(threading.Thread(target=dlimages ,name="thread5" ,args=(5,181)))
threads.append(threading.Thread(target=dlimages ,name="thread6" ,args=(6,213)))
threads.append(threading.Thread(target=dlimages ,name="thread7" ,args=(7,191)))
threads.append(threading.Thread(target=dlimages ,name="thread8" ,args=(8,197)))
threads.append(threading.Thread(target=dlimages ,name="thread9" ,args=(9,170)))
threads.append(threading.Thread(target=dlimages ,name="thread10" ,args=(10,180)))

print len(threads)

for t in threads:
    t.start()
for t in threads:
    t.join()

print "congratulation!"
