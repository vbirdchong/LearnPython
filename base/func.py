
# ��������


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

# ���������ӿ��Կ������������Է��ض��ֵ������ʵ�����ص���һ��tuple�������������ͬʱ����һ��tuple��
# ��λ�ø���Ӧ��ֵ


# Ĭ�ϲ���

def power(x, n=2):
    s = 1
    while n > 0:
        s = s * x
        n = n - 1
    return s

print 'power(5)=%d' % power(5), 'power(5,3)=%d' % power(5,3)


# ��������ʹ��

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

# ע������������������������� END, ����ͺ�����Ƴ��Բ���
#Python�����ڶ����ʱ��Ĭ�ϲ���L��ֵ�ͱ���������ˣ���[]����ΪĬ�ϲ���LҲ��һ��������
#��ָ�����[]��ÿ�ε��øú���������ı���L�����ݣ����´ε���ʱ��Ĭ�ϲ��������ݾͱ��ˣ�
#�����Ǻ�������ʱ��[]�ˡ�


# ʹ�ò��������иĽ�

def add_end2(L=None):
    if L is None:
        L = []
    L.append('END')
    return L

print add_end2()
#['END']
print add_end2()
#['END']



# �ɱ����

#a^2 + b^2 + c^2 + ......

def calc1(number):
    sum = 0
    for n in number:
        sum = sum + n * n
    return sum

print '1^2+2^2+3^3=%d' % calc1([1,2,3])

# ���Ϻ�����ÿ�ε��õ�ʱ�򣬶�Ҫ����װ��һ��list/tuple Ȼ���룬�鷳

# ����ɱ�����Ͷ���list��tuple������ȣ������ڲ���ǰ�����һ��*�š�
##�ں����ڲ�������numbers���յ�����һ��tuple����ˣ�����������ȫ���䡣
##���ǣ����øú���ʱ�����Դ������������������0������
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



## �ؼ��ֲ���
##�ɱ���������㴫��0�����������������Щ�ɱ�����ں�������ʱ�Զ���װΪһ��tuple��
##���ؼ��ֲ��������㴫��0������������������Ĳ�����
##��Щ�ؼ��ֲ����ں����ڲ��Զ���װΪһ��dict

def person(name, age, **kw):
    print 'name:', name, 'age:', age, 'other:', kw

person('Mic', 30)
##name: Mic age: 30 other: {}

person('Lucy', 24, city='uk')
##name: Lucy age: 24 other: {'city': 'uk'}
person('Lili', 22, job='Engineer', city='Shanghai')
##name: Lili age: 22 other: {'city': 'Shanghai', 'job': 'Engineer'}


##���򵥵�д��
kw = {'city':'Beijing', 'job':'Engineer'}
person('Mice', 44, **kw)
##name: Mice age: 44 other: {'city': 'Beijing', 'job': 'Engineer'}



##�������
##��Python�ж��庯���������ñ�ѡ������Ĭ�ϲ������ɱ�����͹ؼ��ֲ�����
##��4�ֲ���������һ��ʹ�ã�����ֻ������ĳЩ��������ע�⣬���������˳������ǣ�
##��ѡ������Ĭ�ϲ������ɱ�����͹ؼ��ֲ���

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



##�ݹ麯��

def fact(n):
    if n == 1:
        return 1
    return n * fact(n-1)

# β�ݹ�
def fact2(n):
    return fact_iter(n,1)

def fact_iter(num, product):
    if num == 1:
        return product
    return fact_iter(num - 1, num * product)

print fact2(5)

#ջ���
print fact2(1000)


# �κεݹ麯��������ջ���������




































