# -*- coding: utf-8 -*-
#按经纬度区块获得不同精度下top照片id列表
#第一步

import json, urllib.request, codecs

def getFun(theStr):
    photos =[]
    index =0
    has_more =True
    while has_more:
        theUrl =r"http://www.panoramio.com/map/get_panoramas.php?set=full&from=" +str(index *100) +r"&to=" +str(index *100 +100) +theStr
        thePage =urllib.request.urlopen(theUrl).read().decode('utf8')
        jsonResult =json.loads(thePage)
        tmpPhotos =jsonResult["photos"]

        # for photo in tmpPhotos:
        #     photoStr =str(photo["photo_id"]) +"\n"
        #     photos.append(photoStr)
        photos +=[str(photo['photo_id']) +'\n' for photo in tmpPhotos]

        has_more =jsonResult["has_more"]
        index += 1
    print((len(photos)))
    return photos

# theIndex =1
# minX = -180
# minY = -90
# #halfUrl =r""
# while minX <180:
#     while minY <90:
#         halfUrl =r"&minx=" +str(minX) +r"&miny=" +str(minY) +r"&maxx=" +str(minX +360) +r"&maxy=" +str(minY +180) +r"&size=medium&mapfilter=false"
#         tmpList =getFun(halfUrl)
#         #写入文件
#         fileName ="e:\\panoramio\\x360y180_1\\%04d_%d_%d_%d_%d" % (theIndex ,minX ,minY ,minX +90 ,minY +45)
#         with codecs.open(fileName, 'w', 'utf-8') as f:
#             f.writelines(tmpList)
#         theIndex +=1
#         minY +=45
#     minX +=90
#     minY =-90

spaceX ,spaceY =90 ,45
l1 =[(x ,y) for x in range(-180 ,180 ,spaceX) for y in range(-90 ,90 ,spaceY)]
urls =["&minx=" +str(x) +"&miny=" +str(y) +"&maxx=" +str(x +spaceX) +"&maxy=" +str(y +spaceY) +"&size=medium&mapfilter=false" for (x ,y) in l1]
files =["/Users/guo/Desktop/x%d_y%d/%04d_%d_%d_%d_%d" % (spaceX ,spaceY ,index ,x ,y ,x +spaceX ,y +spaceY) for (x ,y) ,index in zip(l1 ,range(1 ,len(l1) +1))]
print(len(files))
for url ,file in zip(urls ,files):
    with codecs.open(file, 'w', 'utf-8') as f:
            f.writelines(getFun(url))

#with codecs.open("D:\\panoramio\\panoramio", 'w', 'utf-8') as f:
#    f.writelines(theList)




