#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Aoc 2015 - 00

import sys
sys.path.append('..')
import utils

ISSUE=0

"""
	SOLVE PART 1
"""
def solve_part_1(demo:bool) -> str:

	fn = utils.get_input_file(demo, ISSUE, True)
	print(fn)
	"""Do something here >>>"""

	print('Part 1 not solved yet')

	answer = None

	"""<<< Do something here"""
	utils.print_answer(1, demo, answer)
	return answer

"""
	SOLVE PART 2
"""
def solve_part_2(demo:bool) -> str:

	fn = utils.get_input_file(demo, ISSUE, True)
	print(fn)
	"""Do something here >>>"""

	print('Part 2 not solved yet')

	answer = None

	"""<<< Do something here"""
	utils.print_answer(2, demo, answer)
	return answer

"""
	MAIN
"""
def main(args):

	solve_part_1(1)

	solve_part_2(1)

	return 0

if __name__ == '__main__':
	sys.exit(main(sys.argv))
