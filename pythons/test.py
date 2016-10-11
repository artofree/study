import time, threading ,os

import requests

import json
from datetime import datetime

import configparser

def theFun(tp):
    print(tp[0] ,tp[1])


cf = configparser.ConfigParser()
cf.read(r"C:\Users\guo\Desktop\thePrj\51\conf")
scns =cf.sections()
print(scns)
print(cf.options('db'))
print(cf.items('db'))
theTuple =cf.get('concurrent' ,'thread')
theTuple =json.loads(theTuple)
print(theTuple)
theFun(theTuple)

# now =time.time()
# r =requests.get(url='http://139.219.238.37:8000/gettesttime')
# print(r.text)
# print(now)

# now =datetime.now()
# print(now)
# print(now.strftime('%H:%M:%S.%f'))
# print(int(now.strftime('%S')) +float(now.strftime('%f')[0]) /10)
# print(datetime.now())
# print(time.time())
# index =0
# while index <100:
#     theT =time.time()
#     index +=1
#     time.sleep(0.1 +theT -time.time())
#     # now =datetime.now()
# print(type(time.time()))
# print(datetime.now())

# payload = {'idt': '0001'}
# r = requests.get('http://127.0.0.1:8000/getCode' ,payload)
# print(r.text)


# payload = {'id': 'testuser'}
# files = {'file': open('1.png', 'rb')}
# r = requests.post('http://0.0.0.0:8000/uploadPic', files=files ,data=payload)

# with open('1.png', 'rb') as f:
#     payload = {'id': 'testuser', 'file': f.read()}
#     r = requests.post('http://0.0.0.0:8000/uploadPic' ,data=payload)
#     i =0

# payload = {'username': 'testuser', 'password': 'testuser'}
# r = requests.post('http://127.0.0.1:8000/dologin' ,data=payload)
# i =0
#
#
# # r =requests.get(url='http://127.0.0.1:8000/gettest')
# print(r.status_code)
# print(r.url)
# print(r.text)


# theStr ='sdfyhi  '
# theStr =theStr.strip()
# print(theStr)