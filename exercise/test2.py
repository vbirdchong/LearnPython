#!/usr/bin/evn python
# coding=utf-8

import random

##socre=[]
##for i in range(40):
##    socre.insert(0, random.randint(0,100))

socre = [random.randint(0, 100) for i in range(40)]
print socre

numOfStudent = len(socre)
ave = sum(socre) / numOfStudent
print ave

##badSocre=[]
##for i in socre:
##    if i < ave:
##        badSocre.insert(0, i)

badSocre = [i for i in socre if i < ave]

print badSocre
print "There are %d students less than average:%d" % (len(badSocre), ave)

sorted_socre = sorted(badSocre, reverse=True)
print sorted_socre


