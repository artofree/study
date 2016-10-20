import time ,threading ,myLib

timeStamp =0
threadList =[]

def getTimeStamp():
    global timeStamp
    while 1:
        timeStamp +=1
        time.sleep(1)
        print('subThread:' +str(timeStamp))

def mainWork():
    global threadList
    t = threading.Thread(target=getTimeStamp)
    t.start()
    threadList.append(t)
    while 1:
        print('mainThread' +str(timeStamp))
        time.sleep(1)

def beginWork():
    t = threading.Thread(target=mainWork)
    t.start()
    threadList.append(t)

def clearWork():
    global threadList
    for t in threadList:
        myLib.stop_thread(t)
