#!/usr/bin/env python
# coding = utf-8

# dict 的使用
# 存储方式 使用 key-value 存储

d1 = {'Mic':99, 'Bob':88, 'Lucy':77}

print d1['Mic']

d1['QQ'] = (1,2,3)

d1['Ali'] = (6, [4,5])

print d1

# 如果找不到'JJ' 则返回 error
print d1.get('JJ', 'error')



# set 的使用
# set 是一组key的集合，但不存储value，可以看成数学中元素的集合

s = set([1,2,3])
print s

s.add(1)
print s

s.add(4)
print s

s.add((4,9))
print s

s1 = set([1,2,3,(3,5)])
s2 = set([2,3,4,(3,4)])

print 's1&s2=', s1 & s2, 's1|s2=', s1 | s2


# 简单数据库（人名，电话，地址）

people = {
    'Alice':{
        'phone': '2341',
        'addr': 'Foor drive 23'
    },
    'Beth':{
        'phone': '9210',
        'addr' : 'Bar street 42'
    },
    'Cecil':{
        'phone' : '3158',
        'addr' : 'Baz street 33'
    }
}


labels = {
    'phone' : 'phone number',
    'addr' : 'address'
}

name = raw_input('Name： ')

request = raw_input('Phone number(p) or address(a)? ')

if request == 'p':
    key = 'phone'

if request == 'a':
    key = 'addr'

if name in people:
    print "%s's %s is %s." % (name, labels[key], people[name][key])
else:
    print "Can not find the name:%s" %(name)






