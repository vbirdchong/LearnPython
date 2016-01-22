#!/usr/bin/env python
# coding=utf-8


##a0= 0
##a1=1
##a[n] = a[n-1]+a[n-2]

a = 0
b = 1

for i in range(10):
    a, b = b, a+b

print a
print b


def fibs(rangeValue):
    if rangeValue == 0:
        return 0
    elif rangeValue == 1:
        return 1
    else:
        return fibs(rangeValue-1) + fibs(rangeValue-2)
        
print fibs(10)
