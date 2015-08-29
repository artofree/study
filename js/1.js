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
sdfd = 100;

theArr = [1, 2, 3, 2, 3, 5, 2, 1, 10];
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
    var theArr = 1;
    if (i) {
        i =theArr;
    }
    var myArr = [];
    if (isTrue) {
        myArr["isTrue"] = 1;
    }
    else {
        myArr["isTrue"] = 0;
    }
    return myArr;
}

i =theArr;

var arr = myfun(1);
i = arr['isTrue'];
i = 0;

var val = 0.1 + 0.2;
val = parseFloat("12.4ab");
val = true + "";
var obj;
val = obj && obj.getname();
val = "123" && 123;
if ("123" == val)
    val = 0;

arr = new Array(3);
arr[0] = "George";
arr[1] = "John";
arr[2] = "Thomas";

var arr2 = new Array(3);
arr2[0] = "James";
arr2[1] = "Jhon";
arr2[2] = "Martin";

var arr3 = new Array(2);
arr3[0] = "William";
arr3[1] = "Franklin";

var theArr = arr.concat(arr2, arr3);
i = 0;












