#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# randylampa/AoC2015
# Advent of Code 2015 - 16
# @link https://adventofcode.com/2015/day/16

import sys
import os
cur_dir = os.path.dirname(os.path.realpath(__file__))
par_dir = os.path.dirname(cur_dir)
sys.path.append(par_dir)
import utils
import re

YEAR = 2015
DAY = 16
ISSUE = '16'


def read_file_into_list_of_dict(name = 'input') -> list:
	f = open(name, 'r')
	lines = f.readlines()
	f.close()
	aunts = []
	for line in lines:
		xname,xpar = line.split(':', 1)
		aunt = {
			'name': xname,
			'props': {},
		}
		mm = re.findall('(?P<prop>\w+): (?P<val>\d+)(?:,|$)', xpar)
		for prop,val in mm:
			aunt['props'][prop] = int(val)
		# ~ print(aunt)
		aunts.append(aunt)
	# ~ print(aunts)
	return aunts


'''
	SOLVE PART 1
'''
def solve_part_1(demo:bool) -> str:

	"""Do something here >>>"""

	props_found = utils.read_file_into_dict('input-params16')
	print(props_found)

	aunts = read_file_into_list_of_dict('input16')
	# ~ utils.dump_list_of(aunts)

	aunts_match = []
	for aunt in aunts:
		# ~ print(aunt['name'])
		props = aunt['props']
		match = True
		for k in props:
			match = match and (k in props_found) and (props_found[k] == props[k])
		if match:
			# ~ print("aunt matches")
			aunts_match.append(aunt)
		else:
			# ~ print("aunt DOESNT match")
			pass

	utils.dump_list_of(aunts_match)

	answer = aunts_match[0]['name']

	"""<<< Do something here"""
	utils.print_answer(1, demo, answer)
	return answer


'''
	SOLVE PART 2
'''
def solve_part_2(demo:bool) -> str:

	"""Do something here >>>"""

	props_found = utils.read_file_into_dict('input-params16')
	print(props_found)

	aunts = read_file_into_list_of_dict('input16')
	# ~ utils.dump_list_of(aunts)

	'''
	greater than:	cats, trees
	fewer than:		pomeranians, goldfish
	'''
	aunts_match = []
	for aunt in aunts:
		# ~ print(aunt['name'])
		props = aunt['props']
		matches = True
		for k in props:
			if not k in props_found:
				print("property {} not found".format(k))
				matches = False
				break
			vf = props_found[k]
			v = props[k]
			if k in ['cats', 'trees']:
				# ~ v > vf
				if not v > vf:
					matches = False
					break
			elif k in ['pomeranians', 'goldfish']:
				# ~ v < vf
				if not v < vf:
					matches = False
					break
			else:
				# ~ v = vf
				if not v == vf:
					matches = False
					break
		if matches:
			# ~ print("aunt matches")
			aunts_match.append(aunt)
		else:
			# ~ print("aunt DOESNT match")
			pass

	utils.dump_list_of(aunts_match)

	answer = None

	"""<<< Do something here"""
	utils.print_answer(2, demo, answer)
	return answer

def main():

	# ~ solve_part_1(1)

	solve_part_2(1)

	pass

if __name__ == '__main__':
	sys.exit(main())
