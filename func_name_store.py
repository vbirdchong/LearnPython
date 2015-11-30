#!/usr/bin/env python
# -*- coding = utf-8 -*-

# ���ִ洢�������ļ�ʹ��

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

##ʵ�ֶ������ͬʱ�洢, �ص��� full_namesǰ���Ǻ�, ����ǰ���ǺŽ�����ֵ��������ͬһ��Ԫ�����ռ�����			
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



