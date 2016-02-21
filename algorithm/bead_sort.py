#!/usr/bin/env python
# coding:utf-8

try:
  from itertools import zip_longest
except:
  try:
    from itertools import izip_longest as zip_longest
  except:
    zip_longest = lambda *args: map(None, *args)
 
def beadsort(l):
	print l
	# cl = columns([[1] * e for e in l])
	# print "cl"
	# print cl
	# print "columns"
	# print columns(cl)
	# return map(len, cl)
  	return map(len, columns(columns([[1] * e for e in l])))
 	# return map(len, columns([[1] * e for e in l]))


def columns(l):
  	return [filter(None, x) for x in zip_longest(*l)]
 
# Demonstration code:
print(beadsort([5,3,1,7,4,1,1]))
