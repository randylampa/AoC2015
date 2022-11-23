#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Aoc 2015 - 00

import sys
sys.path.append('..')
import utils

ISSUE=3

def make_list_of_coords(direction_instr, unique:bool=False):
	
	point = (0,0)
	coords = [point]
	for ins in direction_instr:
		#print("ins=",ins)
		if ins=="^":
			point = (point[0], point[1]+1)
		elif ins=="v":
			point = (point[0], point[1]-1)
		elif ins==">":
			point = (point[0]+1, point[1])
		elif ins=="<":
			point = (point[0]-1, point[1])
		else:
			#print("wrong input char")
			continue

		if not unique or unique and not (point in coords):
			#print("add: ins=",ins,"point=",point)
			coords.append(point)
#		else:
#			print("dupl: ins=",ins,"point=",point)

	return coords

def solve_part_1():
	demo = 0

	fn = utils.get_input_file(demo, ISSUE, True);
	print(fn)

	f = open(fn, 'r')
	chars = f.read()
	#print(chars)

	coords = make_list_of_coords(chars, True)
	#print(coords)

	answer = len(coords)

	"""<<< Do something here"""
	utils.print_answer(1, demo, answer)

def solve_part_2():
	demo = 1

	fn = utils.get_input_file(demo, ISSUE, True);
	print(fn)
	"""Do something here >>>"""

	print('Part 2 not solved yet')
	
	answer = None

	"""<<< Do something here"""
	utils.print_answer(2, demo, answer)

def main(args):
	
	solve_part_1()
	
#	solve_part_2()
	
	return 0

if __name__ == '__main__':
	sys.exit(main(sys.argv))
