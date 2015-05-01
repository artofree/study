# -*- coding: utf-8 -*-
#抽取图片统计信息
#photoid,userid,username,userphotos,lt,ltc,ln,lnc,place,photo_title,taken_time,tags,looks,likes,favorites,comments
#其中tags试图与标准tags对应，梳理

import os, urllib2, threading, codecs, time
from pyquery import PyQuery as pq
from lxml import etree

infopath ='E:\\panoramio\\allinfos'
statuspath ='E:\\panoramio\\allstatus'
resultpath ="E:\\panoramio\\parserresult\\16\\10"

for index in range(10,11):
    #用于最终写入文件
    theStrList =[]
    infopath =os.path.join(infopath ,str(index))
    statuspath =os.path.join(statuspath ,str(index))
    infoList =os.listdir(infopath)
    infoSet =set(infoList)
    statusList =os.listdir(statuspath)

    for theFile in statusList:
        if theFile in infoSet:
            listStr = [theFile.split('.')[0]]
            #infos
            filepath =os.path.join(infopath ,theFile)
            if os.path.getsize(filepath) <40000:
                continue
            d = pq(filename=filepath)
            #d = pq(url=r"http://www.panoramio.com/photo/95808783")
            #d = pq(url=r"http://www.panoramio.com/photo/96312089")
            #d = pq(url=r"http://www.panoramio.com/photo/9631201")
            #userid
            content =d("#profile_pic_info a").attr("href")
            if not content:
                continue
            listStr.append(content[content.rfind('/') +1:])
            #username
            content =d("#profile_name a").text()
            listStr.append(content)
            #userphotos
            content =d(".profile-stats-text").text()
            listStr.append(content[:content.find(" ")])
            #lt.ltc
            content =d(".latitude").attr("title")
            listStr.append(content)
            listStr.append(d(".latitude").text())
            #ln,lnc
            content =d(".longitude").attr("title")
            listStr.append(content)
            listStr.append(d(".longitude").text())
            #place
            content =d("#place").text()
            listStr.append(content[content.find('taken in ') +9:])
            #photo_title
            content =d("title").text()
            listStr.append(content[content.find('Photo of ') +9 :])
            #taken_time
            content =d("#tech-details ul li:eq(1)").text()
            listStr.append(content[content.find('Taken on ') +9 :])
            #tags
            tagStr =d("#interim-tags").html()
            dd =pq(tagStr)
            content =dd("li").items()
            tagList =[]
            for x in content:
                tagStr =x.text()
                if tagStr.find("Show all tags") == -1:
                    tagList.append(tagStr)
            listStr.append(','.join(tagList))
            #status
            filepath =os.path.join(statuspath ,theFile)
            if os.path.getsize(filepath) <20000:
                continue
            d = pq(filename=filepath)
            #d = pq(url=r"http://www.panoramio.com/photo/95808783/stats")
            #looks,comments,favorites,likes
            listStr.append(d("#counters li:eq(0) strong").text())
            listStr.append(d("#counters li:eq(1) strong").text())
            listStr.append(d("#counters li:eq(2) strong").text())
            listStr.append(d("#counters li:eq(3) strong").text())
            #写文件
            theStrList.append('||'.join(listStr) +'\n')

    with codecs.open(resultpath, 'a', 'utf-8') as f:
        f.writelines(theStrList)