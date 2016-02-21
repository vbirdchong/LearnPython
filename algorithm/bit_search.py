#!/usr/bin/env python
# coding:utf-8

from quickSort import quick_sort

'''
二分法的搜索需要输入的list为有序数列
bit_search() 使用递归方法实现
bit_search_by_loop() 使用循环实现
'''

def bit_search(list, value, low, high):
	if low > high:
		return -1

	middle = (low + high) / 2
	# print "low:%d, high:%d, value:%d, list[middle]:%d" % (low, high, value, list[middle])
	if list[middle] < value:
		return bit_search(list, value, middle+1, high)
	elif list[middle] > value:
		return bit_search(list, value, low, middle-1)
	else:
		return middle


def bit_search_by_loop(list, value, low, high):
	if low > high:
		return -1

	while(True):
		middle = (low + high) / 2
		if (list[middle] < value):
			low = middle + 1
		elif (list[middle] > value):
			high = middle - 1
		else:
			return middle


if __name__ == '__main__':
	lis = [3, 987, 6, 22, 9, 333, 22, 44, 9999, 555, 999, 1234, 1235, 1255, 1288]
	val = 1235
	sortList = quick_sort(lis)
	ret = bit_search_by_loop(sortList, val, 0, len(lis))
	print sortList
	print ret, lis[ret]

