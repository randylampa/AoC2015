#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Aoc 2015 - 08

import sys
sys.path.append('..')
import utils

ISSUE=8

# ~ def unescape(

def solve_part_1(demo:bool) -> str:

	fn = utils.get_input_file(demo, ISSUE, True)
	print(fn)
	"""Do something here >>>"""

	# load binary and strip ending newline
	lines = utils.read_file_into_list_bin(fn, lambda x:x[:-1])
	# ~ print(lines)
	# ~ exit()

	countsLit = []
	countsMem = []
	for line in lines:
		# ~ print(line)
		countsLit.append(len(line))
		# get rid of quotes and unescape
		value = line[1:-1].decode('unicode_escape')
		# ~ print(value)
		countsMem.append(len(value))

	answer = sum(countsLit) - sum(countsMem)

	"""<<< Do something here"""
	utils.print_answer(1, demo, answer)
	return answer

def solve_part_2(demo:bool) -> str:

	fn = utils.get_input_file(demo, ISSUE, True)
	print(fn)
	"""Do something here >>>"""
	
	lines = utils.read_file_into_list(fn)
	# ~ print(lines)
	# ~ exit()

	countsLit = []
	countsMem = []
	for line in lines:
		# ~ print(len(line), line)
		countsMem.append(len(line))
		# ~ value = line.encode() # not desired results
		value = '"' + line.replace('\\', '\\\\').replace('"', '\\"') + '"'
		# ~ print(len(value), value)
		countsLit.append(len(value))
	
	answer = sum(countsLit) - sum(countsMem)

	"""<<< Do something here"""
	utils.print_answer(2, demo, answer)
	return answer

def main(args):
	
	# ~ solve_part_1(0)
	
	solve_part_2(0)
	
	return 0

if __name__ == '__main__':
	sys.exit(main(sys.argv))
