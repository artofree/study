import time, threading, os

import requests

import json
from datetime import datetime

import configparser

import zipfile
import os

import zipfile
import os

servUrl = 'http://127.0.0.1:8000/'
r = requests.get(servUrl +'getVersionContent', stream=True)
with open(r"/Users/guo/Desktop/2.png", 'wb') as fd:
    for chunk in r.iter_content(10240):
        fd.write(chunk)
# print(requests.get(servUrl +'getVersion').text)
# # servUrl ='http://139.219.238.37:8000/'
# fileUrl =r"/Users/guo/Desktop/1.png"
# files = {'file': open(fileUrl, 'rb')}
# r = requests.post(servUrl +'setVersionContent', files=files)
# print(r.text)

# def zipDir(dirPath, zipPath):
#     zipf = zipfile.ZipFile(zipPath , mode='w')
#     lenDirPath = len(dirPath)
#     for root, _ , files in os.walk(dirPath):
#         for file in files:
#             filePath = os.path.join(root, file)
#             zipf.write(filePath , filePath[lenDirPath :] )
#     zipf.close()
#
#
#
# def unzip(source ,target):
#     source_zip=source
#     target_dir=target
#     myzip=zipfile.ZipFile(source_zip)
#     myfilelist=myzip.namelist()
#     for name in myfilelist:
#         f_handle=open(os.path.join(target_dir, name),"wb")
#         f_handle.write(myzip.read(name))
#         f_handle.close()
#     myzip.close()
#
# zipDir(r"codes/", r"/Users/guo/Desktop/archive.zip")
# time.sleep(2)
# unzip("/Users/guo/Desktop/archive.zip" ,"/Users/guo/Desktop/testdir/")

# import zipfile
#
# z = zipfile.ZipFile('my-archive.zip', 'w', zipfile.ZIP_DEFLATED)
# startdir = "Users/guo/Desktop/taobao/icon"
# for dirpath, dirnames, filenames in os.walk(startdir):
#     for filename in filenames:
#         z.write(os.path.join(dirpath, filename))
# z.close()

#!/usr/bin/env python
# -*- coding: utf-8 -*-

# from zipfile import *
# import zipfile
#
# #解压zip文件


#
# #把整个文件夹内的文件打包
# def adddirfile():
#     f = zipfile.ZipFile('/Users/guo/Desktop/archive.zip','w',zipfile.ZIP_DEFLATED)
#     startdir = r"/Users/guo/Desktop/sikuli"
#     for dirpath, dirnames, filenames in os.walk(startdir):
#         for filename in filenames:
#             f.write(filename)
#     f.close()
#
# adddirfile()
# time.sleep(3)
# unzip()


# cf = configparser.ConfigParser()
# cf.read(r"C:\Users\guo\Desktop\thePrj\51\conf")
# scns =cf.sections()
# print(scns)
# print(cf.options('db'))
# print(cf.items('db'))
# theTuple =cf.get('concurrent' ,'thread')
# theTuple =json.loads(theTuple)
# print(theTuple)
# theFun(theTuple)



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
