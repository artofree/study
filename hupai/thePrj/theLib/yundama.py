import requests
import time, threading ,datetime


theCodeDict ={}
lock = threading.Lock()

def getCode():
    url = 'http://api.yundama.com/api.php?method=upload'
    files = {'file': open(r'C:\Users\guo\Desktop\thePrj\51\1.png', 'rb')}
    data = {'username': 'silentcraft', 'password': 'inwcwizard', 'codetype': '6301', 'appid': '1', 'appkey': '22cc5376925e9387a23cf797cb9ba745'}
    r = requests.post(url, files=files, data=data)
    theCode =r.json()['text']
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

for i in range(1):
    t =threading.Thread(target=getCode)
    t.start()
time.sleep(7)
print(theCodeDict)