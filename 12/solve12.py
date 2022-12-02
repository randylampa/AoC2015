#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Aoc 2015 - 12

import sys
import re
sys.path.append('..')
import utils

ISSUE=12

def open_input() -> str:
	f = open('input{}'.format(ISSUE), 'r')
	return f.read()

"""
	SOLVE PART 1
"""
def solve_part_1(demo:bool) -> str:

	"""Do something here >>>"""

	data = open_input()

	mm = re.findall('-?\d+', data)
	# ~ print(mm)

	numbers = [*map(int, mm)]
	print(numbers)

	answer = sum(numbers)

	"""<<< Do something here"""
	utils.print_answer(1, demo, answer)
	return answer

"""
	SOLVE PART 2
"""
def solve_part_2(demo:bool) -> str:

	"""Do something here >>>"""

	answer = None

	"""<<< Do something here"""
	utils.print_answer(2, demo, answer)
	return answer

"""
	MAIN
"""
def main(args):

	solve_part_1(0)

	# ~ solve_part_2(0)

	return 0

if __name__ == '__main__':
	sys.exit(main(sys.argv))
