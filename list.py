#!/usr/bin/env python
# coding=utf-8

# list 使用

classmates = ['Mic', 'Bob', 'Jim']
print classmates

print len(classmates)

for i in range(len(classmates)):
    print classmates[i]

classmates.append('Lucy')
print classmates
# ['Mic', 'Bob', 'Jim', 'Lucy']

classmates.insert(2, 'Juce')
print classmates
# ['Mic', 'Bob', 'Juce', 'Jim', 'Lucy']

classmates.pop()
print classmates
# ['Mic', 'Bob', 'Juce', 'Jim']


# count 可以用来统计list 中相同字段的个数
classmates.insert(1, 'Jim')
print classmates.count('Jim')


# 另一种list -> tuple, 注意它是用 () 进行定义，这种列表只有 index/count 两种方法
# tuple初始化后就不能更改，属于只读类型，代码更加安全
classmates222 = ('Mic', 'Bob', 'Jim')
print classmates222

print classmates222.index('Bob')

# 如果要定义一个空的tuple
tt = ()
print tt

# 如果要定义一个只有一个元素的 tuple
# 由于1加了括号后可表示tuple 和 数学中的小括号，因此 tuple 增加逗号 "," 来进行区分

# 正确的
t1 = (1,)
print t1

# 错误的
t2 = (1)
print t2



