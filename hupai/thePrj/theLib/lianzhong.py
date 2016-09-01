import requests
import time, threading ,datetime


theCodeDict ={}
lock = threading.Lock()

def getCode():
    url = 'http://bbb4.hyslt.com/api.php?mod=php&act=upload'
    files = {'upload': open(r'C:\Users\guo\Desktop\thePrj\51\1.png', 'rb')}
    data = {'user_name': 'slientcraft', 'user_pw': 'inwcwizard', 'yzmtype_mark': '19'}
    r = requests.post(url, files=files, data=data)
    theCode =r.json()['data']['val']
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