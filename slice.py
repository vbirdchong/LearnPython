#!/usr/bin/env python
# -*- coding=utf-8 -*-

# 对list tuple 进行切片操作，简化元素的选取

L = range(100)
print L

##取前10个数
print L[:10]

##取后10个数
print L[-10:]

##取前10个数，每两个取一个
print L[0:10:2]

##所有数，每5个取一个
print L[::5]

# 对tuple的操作
print (1,2,3,4,5)[:3]
 
print (1,2,3,4,5)[::3]
