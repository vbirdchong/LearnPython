#!usr/bin/env python
# coding=utf-8

# 位图
# 通过random函数随机产生 1000000 个整数，将数据保存于文件中
# 通过列表bit[n] = 1 来表示 0-1000000 的整数集合，而 n 即为所要表示的整数


import random


def generate_data_file():
	try:
		with open('bit_sort_data', 'w') as data_file:
			print "Open success"
			for x in xrange(0,1000000):
				data_file.write(str(random.randint(0, 1000000)) + '\n')

	except IOError as err:
		print "File err: " + str(err)


def save_data_to_file(bit):
	result_num = 0
	try:
		with open('resule_bit_sort_data', 'w') as save_file:
			print "Open the result file"
			for x in xrange(0,1000000):
				if bit[x] == 1:
					save_file.write(str(x) + '\n')
					result_num += 1
	except IOError as err:
		print "File resule_bit_sort_data err: " + str(err)

	return result_num


def get_data(bit):
	try:
		with open('bit_sort_data', 'r') as read_data_file:
			for line in read_data_file:
				num = int(line)
				''' 可以查看满足条件的num '''
				# print num 
				if num < 5000:
					# 将对应num位置的值修改为1，表明该下标处有数值，对应的下标即为该值
					bit[num] = 1
	except IOError, e:
		raise e


if __name__ == '__main__':
	
	bit_value = []
	for x in xrange(0,1000000):
		bit_value.append(0)

	# generate_data_file()
	get_data(bit_value)
	# print bit_value
	print save_data_to_file(bit_value)
	
