#!/usr/bin/env python
# coding = utf-8

from numpy import *
import operator

def createDataSet():
	group = array([[1.0, 1.1],
					[1.0, 1.0],
					[0, 0],
					[0, 0.1]])
	labels = ['A', 'A', 'B', 'B']
	return group, labels


def classify0(inX, dataSet, labels, k):
	dataSetSize = dataSet.shape[0]
	diffMat = tile(inX, (dataSetSize, 1)) - dataSet
	sqDiffMat = diffMat**2
	sqDistances = sqDiffMat.sum(axis=1)
	distances = sqDistances**0.5

	sortedDisIndicies = distances.argsort()
	classCount = {}
	for i in xrange(k):
		voteIlabel = labels[sortedDisIndicies[i]]
		classCount[voteIlabel] = classCount.get(voteIlabel, 0) + 1

	sortedClassCount = sorted(classCount.iteritems(),
								key = operator.itemgetter(1), reverse = True)
	return sortedClassCount[0][0]




def main():
	group, labels = createDataSet()
	print group
	print labels

	print classify0([0.0, 1.2], group, labels, 3)

if __name__ == '__main__':
	main()