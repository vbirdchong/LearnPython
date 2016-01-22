#!/usr/bin/env python
#coding:utf-8

#字符串用法
#raw_input/print 用法
"""
name = raw_input("input your name:")
age = raw_input("Input your age:")

print 'Your name is:', name
print 'Your age is:', int(age)
print 'Your are ' + age + ' years old'
"""

#打印原始字符串
dos = r"c:\news"
print dos

#注意这里的转义字符与上面打印原始字符的区别
dos = "c:\\news"
print dos


#索引的使用
lang = 'study python'
print lang[2]
print lang.index('u')
#字符串的切片
print lang[2:5]

#字符串基本操作
# 1) len() 求序列长度
l = len('hello')
print 'The length of \'hello\':', l

# 2) + 连接2个元素
str1 = 'hello'
str2 = 'word'
print str1 + str2

# 3) * 重复序列元素，跟乘法一样，把某个元素给打印个n编
strhaha = 'Haha '
print strhaha*3

# 4) in 判断元素是否在序列中，返回 True/False
strabc = 'abc'
print 'a' in strabc
print 'z' in strabc


# 5) max() 返回最大值
print max(strabc)

# 6) min() 返回最小值
print min(strabc)


# 7) cmp() 比较
print cmp('a', 'b')
print cmp('a', 'a')
print cmp('b', 'a')
print cmp(1, 2)


#格式化字符串
#string.format() 这个格式化输出非常的直观
y=255
n='Libai'
Str = 'Hangzhou is more than {year}. {name} livs here.'.format(year=y, name=n)
print Str

#字符串的分割
#str.split()
a = 'hello word'
print a.split(' ')


#字符串的拼接
#join() 的使用
a = 'www.baidu.com'
c = a.split('.')
print c
print '.'.join(c)
print '*'.join(c)


#字符编码

print u'中文测试正常'



