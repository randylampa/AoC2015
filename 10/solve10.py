#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Aoc 2015 - 10

import sys
sys.path.append('..')
import utils

ISSUE=10

def look_and_say(inp_str:str) -> str:
	out_str = ""
	pc = None
	cc = 0
	for c in inp_str:
		# ~ print(c)
		if pc is None:
			pc = c; cc = 1; continue # setup
		if c != pc:
			# ~ print(pc, cc)
			out_str += str(cc) + pc # write
			pc = c; cc = 1; continue # reset
		cc+=1
	# ~ print(pc, cc)
	out_str += str(cc) + pc # write leftout
	return out_str

"""
	SOLVE PART 1
"""
def solve_part_1(demo:bool) -> str:

	if demo:
		seq = "1"
		cyc = 5
	else:
		seq = "1113222113"
		cyc = 40
	"""Do something here >>>"""

	print('seq', seq)
	seq1 = seq
	for i in range(cyc):
		seq1 = look_and_say(seq1)
		print('seq1', seq1)
	print("Seq `{}` became `{}` after {} cycles".format(seq, seq1, cyc))

	answer = len(seq1)

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

	solve_part_1(0)

	# ~ solve_part_2(1)

	return 0

if __name__ == '__main__':
	sys.exit(main(sys.argv))
