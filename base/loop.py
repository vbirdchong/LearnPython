# conding = utf-8

# 用这样的方法可以输出4-10之间的数
for i in range(4,10):
    print i

sumNum = 0
sumOdd = 0
for i in range(1, 101, 2):
    sumNum = sumNum + i
    print "sumNum=%d i=%d" % (sumNum, i)


sum = 0
n = 99
while(n>0):
    sum = sum + n
    n = n - 2

print "odd sum=%d" % sum

##name = ''
##while not name:
##	name = raw_input('Please enter your name: ')
##print 'Hello, %s!' % name

##zip 使用

name = ['anne', 'beth', 'gortg', 'damon']
age = [12, 44, 32, 88]

print zip(name, age)
##[('anne', 12), ('beth', 44), ('gortg', 32), ('damon', 88)]
