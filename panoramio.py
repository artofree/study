# -*- coding: utf-8 -*-

import json, urllib2, codecs

def getFun(theStr):
    photos =[]
    index =0
    has_more =True
    while has_more:
        theUrl =r"http://www.panoramio.com/map/get_panoramas.php?set=full&from=" +str(index *100) +r"&to=" +str(index *100 +100) +theStr
        thePage =urllib2.urlopen(theUrl).read()
        jsonResult =json.loads(thePage)
        tmpPhotos =jsonResult["photos"]
        photoStr =""
        for photo in tmpPhotos:
            photoStr =str(photo["photo_id"]) +"\n"
            photos.append(photoStr)
        has_more =jsonResult["has_more"]
        index += 1
    print len(photos)
    return photos

theIndex =3025
minX =0
minY =0
halfUrl =r""
while minX <0:
    while minY <0:
        halfUrl =r"&minx=" +str(minX) +r"&miny=" +str(minY) +r"&maxx=" +str(minX +6) +r"&maxy=" +str(minY +3) +r"&size=medium&mapfilter=false"
        tmpList =getFun(halfUrl)
        #写入文件
        fileName ="D:\\panoramio\\%04d_%d_%d_%d_%d" % (theIndex ,minX ,minY ,minX +6 ,minY +3)
        with codecs.open(fileName, 'w', 'utf-8') as f:
            f.writelines(tmpList)
        theIndex +=1
        minY +=3
    minX +=6
    minY =-90

#with codecs.open("D:\\panoramio\\panoramio", 'w', 'utf-8') as f:
#    f.writelines(theList)




