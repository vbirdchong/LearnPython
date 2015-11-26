#!/usr/bin/env python
# coding = utf-8

# dict ��ʹ��
# �洢��ʽ ʹ�� key-value �洢

d1 = {'Mic':99, 'Bob':88, 'Lucy':77}

print d1['Mic']

d1['QQ'] = (1,2,3)

d1['Ali'] = (6, [4,5])

print d1

# ����Ҳ���'JJ' �򷵻� error
print d1.get('JJ', 'error')



# set ��ʹ��
# set ��һ��key�ļ��ϣ������洢value�����Կ�����ѧ��Ԫ�صļ���

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


# �����ݿ⣨�������绰����ַ��

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

name = raw_input('Name�� ')

request = raw_input('Phone number(p) or address(a)? ')

if request == 'p':
    key = 'phone'

if request == 'a':
    key = 'addr'

if name in people:
    print "%s's %s is %s." % (name, labels[key], people[name][key])
else:
    print "Can not find the name:%s" %(name)






