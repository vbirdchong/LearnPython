#!/usr/bin/evn python
# coding: utf-8

#格式化输出

print 'hello %s, here is your money %d' % ('xiaoming', 100)

print 'hello {0}, here is your money {1}'.format('xiaohong', 99)

# 用这种方法更加的直观
print 'hello {name}, here is your money {money}'.format(name='xiaolin', money=88)
