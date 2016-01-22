#!/usr/bin/env python
# conding=utf-8

__metaclass__  = type


'''
使用迭代的方法实现fibs
'''

##class Fibs:
##    def __init__(self, maxValue):
##        self.max = maxValue
##        self.a = 0
##        self.b = 1
##
##    def __iter__(self):
##        return self
##
##    def next(self):
##        fibs = self.a
##        if fibs > self.max:
##            raise StopIteration
##        self.a, self.b = self.b, self.a + self.b
##        return fibs
##
##
##if __name__ == "__main__":
##    fibs = Fibs(10000)
##    print list(fibs)



'''
使用generator的方法实现fibs
'''

def fibs(maxValue):
    n = 0
    a, b = 0, 1
    while n < maxValue:
        yield a
        a, b = b, a + b
        n += 1

if __name__ == "__main__":
    fib = fibs(10)
    for i in fib:
        print i
