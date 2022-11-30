#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Aoc 2015 - 09

import sys
import re
sys.path.append('..')
import utils

ISSUE=9

def parse_line(line:str) -> dict:
	mm = re.search("(?P<A>\w+) to (?P<B>\w+) = (?P<dist>\d+)", line)
	dm = mm.groupdict()
	dm['dist'] = int(dm['dist'])
	# ~ print(dm)
	return dm
	# ~ return (mm.group(1), mm.group(2), int(mm.group(3)))

def build_city_map(inputs:list) -> dict:
	city_map = {}
	for inp in inputs:
		nA = inp['A']
		nB = inp['B']
		if nA not in city_map:
			city_map[nA] = {}
		if nB not in city_map:
			city_map[nB] = {}
		dA = city_map[nA]
		dB = city_map[nB]
		dA[nB] = inp['dist']
		dB[nA] = inp['dist']
		# ~ print('ooj', dA, dB)
	# ~ print(city_map)
	return city_map

def walk_shortest(city_map:dict, start:str) -> list:
	for dest in city_map[start]:
		dist = city_map[dest]
		print(dist, dest)
		print("{} -> {} = {}".format(start, dest, dist));
	pass

def solve_part_1(demo:bool) -> str:

	fn = utils.get_input_file(demo, ISSUE, True)
	print(fn)
	"""Do something here >>>"""

	inputs = utils.read_file_into_list(fn, parse_line)
	# ~ print(inputs)

	city_map = build_city_map(inputs)
	# ~ print(city_map)

	start = 'London'
	shortest_route = walk_shortest(city_map, start)
	print(shortest_route)

	answer = None

	"""<<< Do something here"""
	utils.print_answer(1, demo, answer)
	return answer

def solve_part_2(demo:bool) -> str:

	fn = utils.get_input_file(demo, ISSUE, True)
	print(fn)
	"""Do something here >>>"""

	print('Part 2 not solved yet')

	answer = None

	"""<<< Do something here"""
	utils.print_answer(2, demo, answer)
	return answer

def main(args):

	solve_part_1(1)

	# ~ solve_part_2(1)

	return 0

if __name__ == '__main__':
	sys.exit(main(sys.argv))
