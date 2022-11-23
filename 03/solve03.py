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
	"""Do something here >>>"""

	f = open(fn, 'r')
	chars = f.read()
	#print(chars)

	coords = make_list_of_coords(chars, True)
	#print(coords)

	answer = len(coords)

	"""<<< Do something here"""
	utils.print_answer(1, demo, answer)

def make_list_of_coords_agents(direction_instr, unique:bool=False, agents:int=1):

	point = (0,0)
	coords = [point]
	
	agent_points = []
	for i in range(agents):
		agent_points.append(point)
	counter = 0
	
	for ins in direction_instr:
		point = agent_points[counter] # load point of current agent
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
			
		agent_points[counter] = point # store point of current agent

		if not unique or unique and not (point in coords):
			#print("add: ins=",ins,"point=",point)
			coords.append(point)
#		else:
#			print("dupl: ins=",ins,"point=",point)

		counter+=1
		if counter>=agents:
			#print("counter wrap")
			counter = 0

	return coords

def solve_part_2():
	demo = 0

	fn = utils.get_input_file(demo, ISSUE, True);
	print(fn)
	"""Do something here >>>"""

	f = open(fn, 'r')
	chars = f.read()
	#print(chars)

	coords = make_list_of_coords_agents(chars, True, 2)
	#print(coords)

	answer = len(coords)

	"""<<< Do something here"""
	utils.print_answer(2, demo, answer)

def main(args):
	
#	solve_part_1()
	
	solve_part_2()
	
	return 0

if __name__ == '__main__':
	sys.exit(main(sys.argv))
