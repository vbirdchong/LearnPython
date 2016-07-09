#!/usr/bin/env python
# coding=utf-8

import copy
import random
from colorama import Fore, Back


def pretty_print(a):
	def color(x):
		if x == 0:
			return Fore.RESET + Back.RESET
		if x == 2:    
			return Fore.RED + Back.RESET
		if x == 4:    
			return Fore.GREEN + Back.RESET
		if x == 8:    
			return Fore.YELLOW + Back.RESET
		if x == 16:   
			return Fore.BLUE + Back.RESET
		if x == 32:   
			return Fore.MAGENTA + Back.RESET
		if x == 64:   
			return Fore.CYAN + Back.RESET
		if x == 128:  
			return Fore.RED + Back.BLACK
		if x == 256:  
			return Fore.GREEN + Back.BLACK
		if x == 512:  
			return Fore.YELLOW + Back.BLACK
		if x == 1024: 
			return Fore.BLUE + Back.BLACK
		if x == 2048: 
			return Fore.MAGENTA + Back.BLACK
		if x == 4096: 
			return Fore.CYAN + Back.BLACK
		if x == 8192: 
			return Fore.WHITE + Back.BLACK

	for i in a:
		for j in i:
			print color(j) + ("%4d" % j) + Fore.RESET + Back.RESET, 
			#print ("%4d" % j),
		print


def random_point(size):
	x = random.randint(0, size)
	y = random.randint(0, size)
	return (x, y)

def random_num(a):
	seed = [2, 2, 4, 4]
	x, y = random_point(len(a) - 1)

	if a[x][y] == 0:
		v = random.randint(0, len(seed) - 1)
		a[x][y] = seed[v]
	else:
		random_num(a)

def random_init(a):
	seed = [2, 2, 2, 4]
	x, y = random_point(len(a) - 1)
	v = random.randint(0, len(seed) - 1)
	a[x][y] = seed[v]

def new_empty_array(size):
	return [[0 for i in range(0, size)] for i in range(0, size)]

def reduce_up(a):
	return rotate(reduce_left(rotate(a)))
	
def reduce_down(a):
	return rotate(reduce_right(rotate(a)))
	
def reduce_left(a):
	return map(reduce_line_left, a)
	
def reduce_right(a):
	return map(reduce_line_right, a)
	
def rotate(a):
	#print "len a", len(a)
	b = new_empty_array(len(a))
	for i in range(0, len(a)):
		for j in range(0, len(a[i])):
			b[i][j] = a[j][i]
	#print b
	return b
'''
	def aux_set(i, j):
		b[i][j] = a[j][i]
	b = new_empty_array(len(a))
	map(lambda i: map(lambda j: aux_set(i, j), range(0, len(a[i]))), range(0, len(a)))
	print "rotate:", b
	return b
'''
	
def reduce_line_left(xs):
	#print "xs:", xs
	def aux(acc, y):
		if len(acc) == 0:
			acc.append(y)
		elif acc[len(acc) - 1] == y:
			acc[len(acc) - 1] = y * 2
			acc.append(0)
		else:
			acc.append(y)
		return acc
	
	# merger two some number
	tmp = reduce(aux, filter(lambda x: x!= 0, xs), [])
	# filter the number not equal to zero
	res = filter(lambda x: x != 0, tmp)
	res.extend([0 for i in range(0, len(xs) - len(res))])
	#print "res", res
	return res
	
def reduce_line_right(xs):
	return reduce_line_left(xs[::-1])[::-1]
	
def is_win(a):
	for i in range(0, len(a)):
		for j in range(0, len(a[i])):
			if a[i][j] == 2048:
				return True
	return False

def is_fail(a):
	for i in range(0, len(a)):
		for j in range(0, len(a[i])):
			if a[i][j] == 0:
				return False
	
	return True
	
def main():
	print "w for move up, a for move left, s for move down, d for move right."
	print "q for quit."
	is_win_state = False
	a = new_empty_array(4)
	random_init(a)
	random_init(a)
	pretty_print(a)
	
	while True:
		b = copy.deepcopy(a)
		key = raw_input()
		if key == "w":
			a = reduce_up(a)
		elif key == "s":
			a = reduce_down(a)
		elif key == "a":
			a = reduce_left(a)
		elif key == "d":
			a = reduce_right(a)
		elif key == "q":
			break
			
		if a == b:
			print "no number to be reduced"
		else:
			random_num(a)
			
		pretty_print(a)
		
		if is_win_state == 0 and is_win(a):
			is_win_state = True
			print "You Win the GAME!!!!!"
		elif is_fail(a):
			print "You Lose the GAME...."
			print "Please Enter 'q' to exit() and retry"
		

def test():
	#print reduce_line_left([4, 4, 2, 4])
	#print reduce_line_left([2,4,2,2])
	#print reduce_line_right([4, 4, 2, 4])
	print reduce_line_right([2,4,2,2])
		
if __name__ == '__main__':
	main()
	#test()