# -*- coding: utf-8 -*-

import json, urllib.request, codecs

def getFun(theStr):
    photos =[]
    index =0
    has_more =True
    while has_more:
        theUrl =r"http://www.panoramio.com/map/get_panoramas.php?set=full&from=" +str(index *100) +r"&to=" +str(index *100 +100) +theStr
        thePage =urllib.request.urlopen(theUrl).read()
        jsonResult =json.loads(thePage)
        tmpPhotos =jsonResult["photos"]
        photoStr =""
        for photo in tmpPhotos:
            photoStr =str(photo["photo_id"]) +"\n"
            photos.append(photoStr)
        has_more =jsonResult["has_more"]
        index += 1
    print(len(photos))
    return photos

theIndex =1
minX = -180
minY = -90
halfUrl =r""
while minX <180:
    while minY <90:
        halfUrl =r"&minx=" +str(minX) +r"&miny=" +str(minY) +r"&maxx=" +str(minX +360) +r"&maxy=" +str(minY +180) +r"&size=medium&mapfilter=false"
        tmpList =getFun(halfUrl)
        #写入文件
        fileName ="e:\\panoramio\\x360y180_1\\%04d_%d_%d_%d_%d" % (theIndex ,minX ,minY ,minX +90 ,minY +45)
        with codecs.open(fileName, 'w', 'utf-8') as f:
            f.writelines(tmpList)
        theIndex +=1
        minY +=45
    minX +=90
    minY =-90

#with codecs.open("D:\\panoramio\\panoramio", 'w', 'utf-8') as f:
#    f.writelines(theList)




