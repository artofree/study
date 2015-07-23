# -*- coding: utf-8 -*-
classmate = []
print((classmate, len(classmate)))
classmate = ["guo", "liao", "chen", "he", 123, None]
print(classmate)
print((classmate[0], len(classmate), classmate[-1]))

classmate[2] = "zhu"
classmate.pop(0)
print((classmate, classmate[2]))

#只要x是非零数值、非空字符串、非空list等，就判断为True，否则为False
x = []
if x:
    print(True)

theStr = "123"
print((theStr, int(theStr)))

theDict = {"guo": 1, "liao": 2, "chen": 3, "he": 4}
print(theDict)
#判断字典是否有某元素
print(("zhu" in theDict))
print((theDict.get("zhu", -1)))
theDict["zhu"] = 5
theDict.pop("chen")
print(theDict)

s = {1, 1, 2, 2, 3, 3, "guo"}
s.add("liao")
print(s)
#s.remove(4)会出错

str1 = "abac"
str2 = str1.replace("a", "A")
print((str2, str1))

#容器生成器
theRange = list(range(0, 100, 5))
print(theRange)

theRange = list(range(10))
print(theRange)
print((theRange[0:2]))
print((theRange[:5]))
print((theRange[-5:]))
print((theRange[-6::2]))

print([x * x for x in range(10) if x %2 ==0])
print([m +n for m in "abc" for n in "xyz"])

import os
#print [d for d in os.listdir("c:\\")]
print([d for d in os.listdir(".")])
print([d for d in os.listdir("..")])
print([k +" = " +str(v) for k ,v in list(theDict.items())])

g =(x * x for x in range(10) if x %2 ==0)
for elem in g:
    print(elem)

#迭代
print("迭代")
for k in theDict:
    print(k)

for v in list(theDict.values()):
    print(v)

for k, v in list(theDict.items()):
    print((k, v))

#set
set1 =set(theRange)
print(set1)
set2 =set(range(5, 15))
print(set2)

set1 |=set2
print(set1)

theList =[1 ,4 ,3 ,7 ,9 ,5, 2]
print((theList.sort()))

#排序
print("排序")
theList =[[1,3,6] ,[5,2,1] ,[8,7,7] ,[9,3,2] ,[7,6,7] ,[4,6,1] ,[8,8,8]]
theList.sort(key=lambda x:(x[1],x[2]) ,reverse=True)
print(theList)
theList.sort(key=lambda col:(col[1]))
print(theList)
theList.remove([8,7,7])
print(theList)

theList =[1,2,5,6,8,0]
theList.sort(reverse=True)
print((theList[0]))

mylist=[5,4,3,2,1]
for i in reversed(mylist):
    print(i)
print(mylist)






















