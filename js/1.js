/**
 * Created by guopeng on 15/5/7.
 */

var theArr = [];
theArr["1"] = 1;
theArr["2"] = 2;

var key = "3";

var val = theArr[key];
if (!val) {
    val = 0;
    if (!val) {
        val = 1;
    }
}
var i = [];
i["a"] = 1;
i = null;
a = 0;

theArr = [1, 2, 3, 1, 3, 5, 8, 1, 10];
for (var x in theArr) {
    if (theArr[x] === 2) {
        theArr.splice(x, 1);
    }
}
theArr["1"] = 1;
theArr["2"] = 2;
i = theArr["1"];
delete theArr["1"];

theObj = Object();
theObj["1"] = 1;
delete theObj["1"];
i = 0;

function sortNumber(a, b) {
    return a[0] - b[0]
}

theArr = [];
theArr.push([31, "1"]);
theArr.push([69, "2"]);
theArr.push([7, "3"]);
theArr.push([48, "4"]);
theArr.push([96, "5"]);

theArr.sort(sortNumber);

theArr = [];
theArr["123"] = 3;
theArr["343"] = 7;
theArr["445"] = 1;
i = theArr.sort();
i = theArr["123"];
i = 0;

function myfun(isTrue) {
    var myArr = [];
    if (isTrue) {
        myArr["isTrue"] = 1;
    }
    else {
        myArr["isTrue"] = 0;
    }
    return myArr;
}

var arr = myfun(1);
i = arr['isTrue'];
i = 0;















