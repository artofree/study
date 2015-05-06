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