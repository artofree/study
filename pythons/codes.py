#各种代码段，不能直接运行

#info 图片
var infowindow = new google.maps.InfoWindow({
        content: '<img src="/static/photos/11533.jpg" width="256" height="256" />',
        position: new google.maps.LatLng(parms.lt, parms.ln)
    });
    infowindow.open(map);

#js，ajax和回调响应：
google.maps.event.addListener(map, 'idle', function () {
        var mapBounds = map.getBounds();
        var ne = mapBounds.getNorthEast();
        var sw = mapBounds.getSouthWest();
        ///请求该区域当前zoom下的图片内容：
        $.getJSON(parms.jsonurl, {
            'nelt': ne.lat(),
            'neln': ne.lng(),
            'swlt': sw.lat(),
            'swln': sw.lng(),
            'zoom': map.getZoom()
        }, function (ret) {
            //返回值 ret 在这里是一个列表
            //for(var index =0 ;index <ret.length ;index ++) {
            var bigPhotos = ret[0];
            var smallPhotos = ret[1];

            for (var index = 0; index < smallPhotos.length; index++) {
                var thePhoto = smallPhotos[index];
                var myLatLng = new google.maps.LatLng(Number(thePhoto[1]), Number(thePhoto[2]));
                var beachMarker = new google.maps.Marker({
                    position: myLatLng,
                    map: map,
                    icon: thePhoto[0]
                    //icon:"/static/tinis/25855184.jpg"
                });
            }

            for (var index = 0; index < bigPhotos.length; index++) {
                var thePhoto = bigPhotos[index];
                var myLatLng = new google.maps.LatLng(Number(thePhoto[1]), Number(thePhoto[2]));
                var beachMarker = new google.maps.Marker({
                    position: myLatLng,
                    map: map,
                    icon: thePhoto[0]
                    //icon:"/static/tinis/25855184.jpg"
                });
            }
        })
    });

///对应前端推送模型！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！
var source = new EventSource("/getTilesInfo/");
source.onmessage = function (event) {
    if (event.data == "")
        return;
    var data = JSON.parse(event.data);
    for (var i1 = 0; i1 < data.length; i1++) {
        var ret = data[i1];
        if (allLayer[Number(ret["zoom"])] === undefined) {
            //allLayer[Number(ret["zoom"])] = [];
            continue
        }
        var theLayer = allLayer[Number(ret["zoom"])];
        for (var i2 = 0; i2 < theLayer.length; i2++) {
            if (theLayer[i2]["x"] == Number(ret["x"]) && theLayer[i2]["y"] == Number(ret["y"]))
                return;
        }
        var theTile = [];
        theTile["x"] = Number(ret["x"]);
        theTile["y"] = Number(ret["y"]);
        var nepoint1 = new google.maps.LatLng(Number(ret["nelt"]), Number(ret["neln"]));
        var swpoint1 = new google.maps.LatLng(Number(ret["swlt"]), Number(ret["swln"]));
        theTile["rect"] = new google.maps.LatLngBounds(swpoint1, nepoint1);
        var elements = ret["elements"];
        for (var i = 0; i < elements.length; i++) {
            var theElement = [];
            theElement["photoid"] = elements[i][0];
            var nepoint = new google.maps.LatLng(Number(elements[i][1]), Number(elements[i][2]));
            var swpoint = new google.maps.LatLng(Number(elements[i][3]), Number(elements[i][4]));
            theElement["rect"] = new google.maps.LatLngBounds(swpoint, nepoint);
            theElement["point"] = new google.maps.LatLng(Number(elements[i][5]), Number(elements[i][6]));
            theTile.push(theElement);
        }
        theLayer.push(theTile);
    }
};

#后端推送tile的cell信息,已废
def getTilesInfo(request):
    global tilesInfo
    if len(tilesInfo) >0:
        data = json.dumps(tilesInfo)
        tilesInfo =[]
        #del tilesInfo[:]
        response =HttpResponse('data:%s\n\nretry:1000\n' % data,content_type='text/event-stream')
        response['Cache-Control'] = 'no-cache'
        return response
    else:
        return HttpResponse('data:\n\nretry:1000\n',content_type='text/event-stream')

#返回某区域全部图片，已废
def getPhotos(request):
    nelt =float(request.GET['nelt'])
    neln =float(request.GET['neln'])
    swlt =float(request.GET['swlt'])
    swln =float(request.GET['swln'])
    zoom =int(request.GET['zoom'])
    bigSet =set()
    smallSet =set()
    bigUrl ='/static/smalls/'
    smallUrl ='/static/tinis/'
    #bigUrl ='/photo/small/'
    #smallUrl ='/photo/tiny/'
    fileTail ='.jpg'
    bigPhotos =[]
    smallPhotos =[]

    pd.choosePhotos(rootCell ,nelt ,swlt ,neln ,swln ,zoom ,bigSet ,smallSet)
    for cell in bigSet:
        bigPhotos.append([bigUrl +str(cell.cphoto.testid) +fileTail ,cell.cphoto.lt ,cell.cphoto.ln])
    for cell in smallSet:
        smallPhotos.append([smallUrl +str(cell.cphoto.testid) +fileTail ,cell.cphoto.lt ,cell.cphoto.ln])

    thePhotos =[bigPhotos ,smallPhotos]
    return JsonResponse(thePhotos ,safe=False)

#简化：主节点到基本层以上所有节点全部返回
def choosePhotos(rootCell ,nelt, swlt ,neln ,swln ,zoom ,bigSet ,smallSet):
    desRect =ltlnrect(nelt, swlt ,neln ,swln)
    parentCell =rootCell.findFitCell(desRect)
    parentCell.getDeepAllCell(zoom -1 ,bigSet)
    listOut =[theCell for theCell in bigSet if not desRect.ptInRect(theCell.cphoto.lt ,theCell.cphoto.ln)]
    bigSet -=set(listOut)
    parentCell.getDeepAllCell(zoom +2 ,smallSet)
    listOut =[theCell for theCell in smallSet if not desRect.ptInRect(theCell.cphoto.lt ,theCell.cphoto.ln)]
    smallSet -=set(listOut)
    smallSet -=bigSet



