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

##实现多个名字同时存储, 重点是 full_names前的星号, 参数前的星号将所有值都放置在同一个元组中收集起来			
def name_storeV2(data, *full_names):
        for full_name in full_names:
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

name_storeV2(MyNames, 'Luke Skywalker', 'Anakin Skywalker')
print lookup(MyNames, 'last', 'Skywalker')



