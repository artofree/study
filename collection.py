# -*- coding: utf-8 -*-
classmate = []
print classmate, len(classmate)
classmate = ["guo", "liao", "chen", "he", 123, None]
print classmate
print classmate[0], len(classmate), classmate[-1]

classmate[2] = "zhu"
classmate.pop(0)
print classmate, classmate[2]

#只要x是非零数值、非空字符串、非空list等，就判断为True，否则为False
x = []
if x:
    print 'True'

theRange = range(0, 100, 5)
print theRange

theStr = "123"
print theStr, int(theStr)

theDict = {"guo": 1, "liao": 2, "chen": 3, "he": 4}
print theDict
print theDict.get("zhu", -1)
theDict["zhu"] = 5
theDict.pop("chen")
print theDict

s = {1, 1, 2, 2, 3, 3, "guo"}
print s
#s.remove(4)会出错

str1 = "abac"
str2 = str1.replace("a", "A")
print str2, str1























