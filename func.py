
# 函数定义


def sayHello():
    print("Hello World")


def max(a,b):
    if a > b:
        return a
    else:
        return b


sayHello()
print(max(1,2))


import math

def my_move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y + step * math.sin(angle)
    return nx, ny

newX, newY = my_move(100, 100, 60, math.pi / 6)
print 'newX={x}, newY={y}'.format(x=newX, y= newY)

r = my_move(100, 100, 60, math.pi / 6)
print r
# (151.96152422706632, 130.0)

# 从以上例子可以看出，函数可以返回多个值，但其实他返回的是一个tuple，多个变量可以同时接受一个tuple，
# 按位置给对应的值


# 默认参数

def power(x, n=2):
    s = 1
    while n > 0:
        s = s * x
        n = n - 1
    return s

print 'power(5)=%d' % power(5), 'power(5,3)=%d' % power(5,3)


# 不变对象的使用

def add_end1(L=[]):
    L.append('END')
    return L

print add_end1([1,2,3])
##[1, 2, 3, 'END']
print add_end1(['x','y','z'])
##['x', 'y', 'z', 'END']
print add_end1()
##['END']
print add_end1()
##['END', 'END']

# 注意上面的这个输出结果，输出两个 END, 这个和函数设计初衷不符
#Python函数在定义的时候，默认参数L的值就被计算出来了，即[]，因为默认参数L也是一个变量，
#它指向对象[]，每次调用该函数，如果改变了L的内容，则下次调用时，默认参数的内容就变了，
#不再是函数定义时的[]了。


# 使用不变对象进行改进

def add_end2(L=None):
    if L is None:
        L = []
    L.append('END')
    return L

print add_end2()
#['END']
print add_end2()
#['END']



# 可变参数

#a^2 + b^2 + c^2 + ......

def calc1(number):
    sum = 0
    for n in number:
        sum = sum + n * n
    return sum

print '1^2+2^2+3^3=%d' % calc1([1,2,3])

# 以上函数在每次调用的时候，都要先组装出一个list/tuple 然后传入，麻烦

# 定义可变参数和定义list或tuple参数相比，仅仅在参数前面加了一个*号。
##在函数内部，参数numbers接收到的是一个tuple，因此，函数代码完全不变。
##但是，调用该函数时，可以传入任意个参数，包括0个参数
def calc2(*number):
    sum = 0
    for n in number:
        sum = sum + n * n
    return sum
print 'upgrade 1^2+2^2+3^2=%d' % calc2(1,2,3)

nums1 = [1,2,3]
print 'nums1 = %d' % calc2(*nums1)

nums2 = (4,5,6)
print 'nums2 = %d' % calc2(*nums2)



## 关键字参数
##可变参数允许你传入0个或任意个参数，这些可变参数在函数调用时自动组装为一个tuple。
##而关键字参数允许你传入0个或任意个含参数名的参数，
##这些关键字参数在函数内部自动组装为一个dict

def person(name, age, **kw):
    print 'name:', name, 'age:', age, 'other:', kw

person('Mic', 30)
##name: Mic age: 30 other: {}

person('Lucy', 24, city='uk')
##name: Lucy age: 24 other: {'city': 'uk'}
person('Lili', 22, job='Engineer', city='Shanghai')
##name: Lili age: 22 other: {'city': 'Shanghai', 'job': 'Engineer'}


##更简单的写法
kw = {'city':'Beijing', 'job':'Engineer'}
person('Mice', 44, **kw)
##name: Mice age: 44 other: {'city': 'Beijing', 'job': 'Engineer'}



##参数组合
##在Python中定义函数，可以用必选参数、默认参数、可变参数和关键字参数，
##这4种参数都可以一起使用，或者只用其中某些，但是请注意，参数定义的顺序必须是：
##必选参数、默认参数、可变参数和关键字参数

def funcABC(a, b, c=0, *args, **kw):
    print 'a=',a, 'b=',b, 'c=',c, 'args=',args, 'kw=',kw

funcABC(1,2)
##a= 1 b= 2 c= 0 args= () kw= {}

args = (9,8,7,6)
kw = {'A':99, 'B':88, 'C':77}
funcABC(*args, **kw)
##a= 9 b= 8 c= 7 args= (6,) kw= {'A': 99, 'C': 77, 'B': 88}

funcABC(11,22,33, *args, **kw)
##a= 11 b= 22 c= 33 args= (9, 8, 7, 6) kw= {'A': 99, 'C': 77, 'B': 88}



##递归函数

def fact(n):
    if n == 1:
        return 1
    return n * fact(n-1)

# 尾递归
def fact2(n):
    return fact_iter(n,1)

def fact_iter(num, product):
    if num == 1:
        return product
    return fact_iter(num - 1, num * product)

print fact2(5)

#栈溢出
print fact2(1000)


# 任何递归函数都存在栈溢出的问题




































