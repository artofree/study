# -*- coding: utf-8 -*-
import theLib.damatu as td
import time, threading ,datetime


theCodeDict ={}
lock = threading.Lock()

def getCode():
    dmt=td.DamatuApi("slientcraft","inwcwizard")
    # d1 =datetime.datetime.now()
    theCode =dmt.decode(r'C:\Users\guo\Desktop\thePrj\51\1.png',200)
    # d2 =datetime.datetime.now()
    # print(theCode ,(d2 -d1).microseconds)
    print(theCode)
    lock.acquire()
    try:
        global theCodeDict
        if theCode in theCodeDict:
            theCodeDict[theCode] +=1
        else:
            theCodeDict[theCode] =1
    finally:
        lock.release()

for i in range(10):
    t =threading.Thread(target=getCode)
    t.start()
time.sleep(7)
print(theCodeDict)
# theCodeDict = sorted(theCodeDict.items(), key=lambda dic: dic[1])
# print(theCodeDict[-1][0])

