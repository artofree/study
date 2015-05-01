# -*- coding: utf-8 -*-
import os, urllib2, threading, codecs, time
from pyquery import PyQuery as pq
from lxml import etree

infopath ='E:\\panoramio\\allinfos'
statuspath ='E:\\panoramio\\allstatus'
resultpath ="E:\\panoramio\\parserresult\\names"
theCount =0
for index in range(1,2):
    #用于最终写入文件
    nameSet =set()
    infopath =os.path.join(infopath ,str(index))
    statuspath =os.path.join(statuspath ,str(index))
    infoList =os.listdir(infopath)
    infoSet =set(infoList)
    statusList =os.listdir(statuspath)

    for theFile in statusList:
        if theFile in infoSet:
            theCount +=1
            print theCount
            #infos
            filepath =os.path.join(infopath ,theFile)
            if os.path.getsize(filepath) <40000:
                continue
            d = pq(filename=filepath)
            #d = pq(url=r"http://www.panoramio.com/photo/95808783")
            #d = pq(url=r"http://www.panoramio.com/photo/96312089")
            #d = pq(url=r"http://www.panoramio.com/photo/9631201")
            #username
            content =d("#profile_name a").text()
            if len(content) >15:
                continue
            theStr =content.lower()
            tag =True
            for x in theStr:
                if x not in ['a','b','c','d' ,'e','f','g' ,'h','i','j' ,'k','l','m' ,'n','o','p' ,'q','r','s' ,'t','u','v' ,'w','x','y' ,'z','0','9' ,'8','7','6' ,'5','4','3' ,'2','1']:
                    tag =False
                    break
            if tag:
                nameSet.add(content +'\n')

    #写文件
    with codecs.open(resultpath, 'a', 'utf-8') as f:
        f.writelines(nameSet)