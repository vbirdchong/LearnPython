#!/usr/bin/env python
# -*- coding = utf-8 -*-

# 名字存储，函数的简单使用

def init(data):
	data['first'] = {}
	data['middle'] = {}
	data['last'] = {}


def lookup(data, label, name):
	return data[label].get(name)


def name_store(data, full_name):
	names = full_name.split()
	
	if len(names) == 2:
		names.insert(1, '')
		
	labels = ('first', 'middle', 'last')
	
	for label, name in zip(labels, names):
		people = lookup(data, label, name)
		if people:
			people.append(full_name)
		else:
			data[label][name] = [full_name]
			
			
MyNames = {}
init(MyNames)
name_store(MyNames, 'Magnus Lie Hetland')
print lookup(MyNames, 'middle', 'Lie')

