# -*- coding: utf-8 -*-

###str:
str1 = "abac"
str2 = str1.replace("a", "A")
print(str2, str1)

###tuple:
t1 =1 ,2 ,3 ,4 ,5
t2 =('a' ,'b' ,'c')
print(t1 +t2)
print(t1 ,t2)
x ,y ,z =t2
print (x , y ,z)


#list:
classmate = []
print((classmate, len(classmate)))
classmate = ["guo", "liao", "chen", "he", 123, None]
print(classmate)
print(classmate[0], len(classmate), classmate[-1])

classmate[2] = "zhu"
classmate.pop(0)
print((classmate, classmate[2]))
#必须数量匹配
a ,b ,c ,d ,e =classmate
print (c)
begin ,*middle ,end =classmate
print(middle)

print (classmate.index('zhu'))
s1 ='_'.join(classmate[:3])
print(s1)
print(s1.split('_'))

#dict
theDict = {"guo": 1, "liao": 2, "chen": 3, "he": 4}
print(theDict)
#判断字典是否有某元素
print(("zhu" in theDict))
print((theDict.get("zhu", -1)))
theDict["zhu"] = 5
theDict.pop("chen")
print(theDict)
print(theDict.keys())
print(sorted(theDict.keys()))

for k in theDict:
    print(k)

for v in list(theDict.values()):
    print(v)

for k, v in list(theDict.items()):
    print((k, v))

d1 =dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])
print(d1)
d1 ={x: x**2 for x in (2, 4, 6)}
print(d1)
#仅适用于字符串关键字：
d1 =dict(sape=4139, guido=4127, jack='jack')
print(d1)
#字典排序：
prices = {'ACME': 45.23,'AAPL': 612.78,'IBM': 205.55,'HPQ': 37.20,'FB': 10.75}
prices_sorted = sorted(zip(prices.values(), prices.keys()))
print(prices_sorted)
#字典生成器
tech_names = {'AAPL', 'IBM', 'HPQ'}
p2 = {key: value for key, value in prices.items() if key in tech_names}
print(p2)
#字典组合
a = {'x': 1, 'z': 3 }
b = {'y': 2, 'z': 4 }
from collections import ChainMap
c =ChainMap(a ,b)
print(c['y'])


###set
#想要创建空集合，你必须使用 set() 而不是 {}。后者用于创建空字典
set1 =set(range(10))
print(set1)
set2 =set(range(5, 15))
print(set2)

print (set1 ^set2)
set1 |=set2
print(set1)

theList =[1 ,4 ,3 ,7 ,9 ,5, 2]
print((theList.sort()))

s1 =set('adfnadfad')
print (s1)
s1 ={x for x in 'adfdfvnjvk' if x not in 'abcd'}
print(s1)

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

mylist=[5,3,1,2,4]
for i in reversed(mylist):
    print(i)
print(mylist)

t =1 ,2 ,3
print(t)

#高级内容
theRange = list(range(0, 100, 5))
print(theRange)

print([x * x for x in range(10) if x %2 ==0])
print([m +n for m in "abc" for n in "xyz"])

import os
#print [d for d in os.listdir("c:\\")]
print([d for d in os.listdir(".")])
print([d for d in os.listdir("..")])

vec = [[1,2,3], [4,5,6], [7,8,9]]
print([num for elem in vec for num in elem])
#wrong:print([num for num in elem for elem in vec])
print([[x **2 for x in row] for row in vec])

v1 =[1 ,2 ,3 ,4 ,5]
v2 =[1 ,2 ,3 ,4 ,5]
print([(lambda x ,y :x *y)(x ,y) for x in v1 for y in v2])
v =list(map(lambda x :print(x) ,v1))
print(v)

spaceX ,spaceY =90 ,45
l1 =[(x ,y) for x in range(-180 ,180 ,spaceX) for y in range(-90 ,90 ,spaceY)]
print(l1)
l2 =[x +y for (x ,y) in l1]
print(l2)

for (x1 ,x2) ,x3 in zip(l1 ,range(16)):
    print (x1 ,x2 ,x3)

###容器转换
d1 =dict(zip(v1 ,v2))























