import time, threading ,os

import requests

import json
from datetime import datetime

print(datetime.now().timestamp())


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
# # r =requests.get(url='http://127.0.0.1:8000')
# print(r.status_code)
# print(r.url)
# print(r.text)


# theStr ='sdfyhi  '
# theStr =theStr.strip()
# print(theStr)