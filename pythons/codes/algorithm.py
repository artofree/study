# -*- coding: utf-8 -*-

###求质数
for n in range(2 ,100):
    for x in range(2 ,n):
        if n %x ==0:
            print (n ,'equals' ,x ,'*' ,n//x)
            break
    else:
        print (n ,'is a prime number')

###斐波那契数列
def fib(n):
    a ,b ,index=0 ,1 ,0
    while index <n:
        print (a ,end=' ')
        a ,b ,index =b ,a +b ,index +1

fib(10)
print("end")
#全局变量使用：
gCount =100
def fun():
    # global gCount
    gCount =10
    print(gCount)

fun()
print(gCount)

#递归，汉诺塔
def move(n, a, b, c):
    if n == 1:
        print (a+'-->'+c)
    else:
        move(n-1,a,c,b)
        print (a+'-->'+c)
        move(n-1,b,a,c)

move(5, 'A', 'B', 'C')

gCount =1
def hanno(n ,a , b, c):
    if n >=1:
        hanno(n -1 ,a ,c ,b)
        global gCount
        print(str(gCount) +': ' +a +'-->' +c)
        gCount +=1
        hanno(n -1 ,b ,a ,c)
hanno(5 ,'a' ,'b' ,'c')

###