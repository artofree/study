/**
 * Created by guopeng on 15/5/7.
 */
var minleftwidth =5;
var comrightwidth =500;
var safeblank =10;
var rightpadding =20;
var tabheight =30;
var navheight =50;
var navtopmargin =100;
function myFun() {
    var rightWidth;
    var leftWidth;
    var width = $(window).width();
    var thumbdiv =$("#thumbdiv");
    thumbdiv.empty();
    if (width > comrightwidth +safeblank +minleftwidth) {
        rightWidth = comrightwidth -2*rightpadding;
        leftWidth = width - comrightwidth -safeblank;
    }
    if (width <= comrightwidth +safeblank +minleftwidth) {
        leftWidth = minleftwidth;
        rightWidth = width - safeblank -minleftwidth -2*rightpadding;
    }
    $("#mapdiv").width(leftWidth);
    var rightdiv =$("#rightdiv");
    rightdiv.width(rightWidth);
    $("#tabdiv").height(tabheight);
    var navdiv =$("#navdiv");
    navdiv.height(navheight);
    thumbdiv.height(rightdiv.height() -tabheight -navheight -navtopmargin);

    ///计算图片元素个数
    var theHeight =thumbdiv.height();
    var theWidth =thumbdiv.width();
    var theCount =Math.floor(theHeight/112) *Math.floor(theWidth/112);
    for(var index =0; index <theCount ;index++){
        thumbdiv.append('<div style="float: left ;height: 114px ;width: 114px">' +
        '<img src="http://mw2.google.com/mw-panoramio/photos/thumbnail/48619132.jpg" style="background: rgb(255, 255, 255);">' +
        '</div>');
    }
}

function createPhotoCell() {

}

$(document).ready(function () {
    $(window).resize(function () {
        myFun()
    });
});

$(document).ready(function () {
    myFun()
});