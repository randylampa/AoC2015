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

def solve_part_1(demo:bool) -> str:

	fn = utils.get_input_file(demo, ISSUE, True)
	print(fn)
	"""Do something here >>>"""

	inputs = utils.read_file_into_list(fn, parse_line)
	# ~ print(inputs)

	city_map = {}
	cm_def = {
		'name': None,
		'dists': {},
	}
	for inp in inputs:
		nA = inp['A']
		nB = inp['B']
		if nA not in city_map:
			city_map[nA] = {
				'name': nA,
				'dists': {},
			}
		if nB not in city_map:
			city_map[nB] = {
				'name': nB,
				'dists': {},
			}
		dA = city_map[nA]
		dB = city_map[nB]
		dA['dists'][nB] = inp['dist']
		dB['dists'][nA] = inp['dist']
		# ~ print('ooj', dA, dB)
	print(city_map)

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
