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


def read_file_into_dict(name = 'input') -> dict:
	"""
	Reads all lines into dict and map mapfnc on each.
	"""
	outdict = {}
	f = open(name, 'r')
	lines = f.readlines()
	f.close()
	for line in lines:
		k,v = map(lambda x:x.strip(), line.split(':'))
		outdict[k] = v
	return outdict

def read_file_into_list_of_dict(name = 'input') -> list:
	outdict = {}
	f = open(name, 'r')
	lines = f.readlines()
	f.close()
	for line in lines:
		pass
	pass

def parseParams()->dict:
	return read_file_into_dict('input-params16')


'''
	SOLVE PART 1
'''
def solve_part_1(demo:bool) -> str:

	fn = utils.get_input_file(1 if demo else 0, DAY, YEAR)
	print(fn)
	fl = cur_dir + '/' + fn
	"""Do something here >>>"""

	params = parseParams()
	print(params)

	answer = None

	"""<<< Do something here"""
	utils.print_answer(1, demo, answer)
	return answer


'''
	SOLVE PART 2
'''
def solve_part_2(demo:bool) -> str:

	fn = utils.get_input_file(1 if demo else 0, DAY, YEAR)
	print(fn)
	fl = cur_dir + '/' + fn
	"""Do something here >>>"""

	answer = None

	"""<<< Do something here"""
	utils.print_answer(2, demo, answer)
	return answer

def main():

	solve_part_1(1)

	# ~ solve_part_2(1)

	pass

if __name__ == '__main__':
	sys.exit(main())
