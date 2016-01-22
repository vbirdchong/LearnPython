# -*- coding: utf-8 -*-
# hello.py

#name = raw_input('please input your name:\n')
#print 'hello', name

#print a values

a = -4
if a >= 0:
	print a 
else:
	print -a

names= ["Chen", "Bob", "Tim"]
for name in names:
        print name

sum = 0
for x in [1,2,3,4,5,6,7,8,9,10]:
        sum = sum + x
print sum

sum = 0
for x in range(101):
        sum = sum + x
print sum

sum = 0
n = 100
while n > 0:
        sum = sum + n
        n = n - 1
print sum

##判断循环使用方法
##sum = 0
##endvalue = int(raw_input('input endvalue: '))
##if endvalue > 0:
##        while endvalue > 0:
##                sum = sum + endvalue
##                endvalue = endvalue - 1
##        print 'total sum:%d' % sum
##else:
##        print 'do not support\n'


##use dict and set function
d = {'Michacel':95, 'Bob':75, 'Tracy':85}
print d

##instert a key
d['Jim'] = 100
print d

##determine a key in dict
if ('Bob' in d):
        print 'Bob is in dict -->true\n'
else:
        print 'Bob is not in dict -->false\n'

##delete a key from dict
print d
d.pop('Bob')
print d


s1 = set([1,2,3])
s2 = set([2,3,4])
s3 = set(['a','b'])
s4 = set(['b','c'])

##function
def my_abs(x):
        if not isinstance(x, (int, float)):
                raise TypeError('bad operand type')
        if x >= 0:
                return x
        else:
                return -x

print my_abs(-2)
##print my_abs('a')

##可变参数函数
def calc(*numbers):
        sum = 0
        for n in numbers:
                sum = sum + n * n
        return sum


##关键字参数
def person(name, age, **kw):
        print 'name:', name, 'age:', age, 'other:', kw

##递归函数
##def fact(n):
##        if n == 1:
##                return 1
##        print ' %d ' % n, ' * ', 'fact(%d)\n' % (n - 1)
##        return n * fact(n-1)

##尾递归
def fact(n):
        return fact_iter(1,1,n)

def fact_iter(product, count, max):
        if count > max:
                return product
        return fact_iter(product * count, count + 1, max)
