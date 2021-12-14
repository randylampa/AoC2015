#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Aoc 2015 - 01

import sys
sys.path.append('..')
import utils

ISSUE=1

def solve_part_1():
	demo = 0

	fn = utils.get_input_file(demo, ISSUE);
	print(fn)
	"""Do something here >>>"""
	f = open(fn, 'r')
	data = f.read().strip()
	f.close()
	print(data)
	
	floor = 0
	for d in data:
		if d=='(':
			floor+=1
		elif d==')':
			floor-=1
	
	answer = floor
	
	"""<<< Do something here"""
	utils.print_answer(1, demo, answer)

def solve_part_2():
	demo = 0

	fn = utils.get_input_file(demo, ISSUE);
	print(fn)
	"""Do something here >>>"""
	f = open(fn, 'r')
	data = f.read().strip()
	f.close()
	print(data)
	
	floor = 0
	pos = 0
	for d in data:
		pos+=1
		if d=='(':
			floor+=1
		elif d==')':
			floor-=1
		if floor<0:
			print('entering basement! at instruction no.{}'.format(pos))
			break
	
	answer = pos
	
	"""<<< Do something here"""
	utils.print_answer(2, demo, answer)

def main(args):
	
	#~ solve_part_1()
	
	solve_part_2()
	
	return 0

if __name__ == '__main__':
	sys.exit(main(sys.argv))
