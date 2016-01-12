__metaclass__ = type

'''
迭代器实现斐波那契数列
'''

class Fibs:
    def __init__(self):
        self.a = 0
        self.b = 1

    def next(self):
        self.a, self.b = self.b, self.a + self.b
        return self.a

    def __iter__(self):
        return self


fibs = Fibs()

for f in fibs:
    if f < 50:
        print f
        #break
    else:
        break


'''
实际上，因为迭代操作如此普遍，Python专门将关键字for用作了迭代器的语法糖。
在for循环中，Python将自动调用工厂函数iter()获得迭代器，自动调用next()获取元素，
还完成了检查StopIteration异常的工作
'''

listA = [1,2,3]

it = iter(listA)
try:
    while True:
        val = it.next()
        print val
except StopIteration:
    pass

##一个for循环解决上面好几个步骤
for value in listA:
    print value




