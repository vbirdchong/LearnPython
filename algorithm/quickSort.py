#!/usr/bin/env python
# coding:utf-8

'''
快速排序方法，选取一个基准值后，将无序列表分为左右两个子列表，
左表为小于基准值，右表为大于基准值，
之后将左右表各自再进行递归排序
'''
def quick_sort(arry):
	if len(arry) <= 1:
		return arry

	# 小于基准值的列表
	lessList = []
	# 基准列表，该列表在第一轮选取后就不需要再进行排序变更
	piovtList = []
	# 大于基准值的列表
	moreList = []

	# 选取第一个值最为基准值来进行判断
	piovtValue = arry[0]
	for i in arry:
		if piovtValue > i:
			lessList.append(i)
		elif piovtValue < i:
			moreList.append(i)
		else:
			piovtList.append(i)

	# 将本轮过滤出来的值再进行递归排序
	lessList = quick_sort(lessList)
	moreList = quick_sort(moreList)

	return lessList + piovtList + moreList

if __name__ == '__main__':
	print 'In quick_sort moduel'