#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Aoc 2015 - 06

import sys
sys.path.append('..')
import utils

ISSUE=6

gridsize = 1000
light_grid = [[0] * gridsize] * gridsize
# ~ print(light_grid)

def grid_apply(begin:tuple, end:tuple, cmd:str):
	for x in range(begin[0], end[0]):
		for y in range(begin[1], end[1]):
			val = light_grid[x][y]
			if cmd == 'toggle':
				light_grid[x][y] = 0 if val==1 else 1
			else:
				light_grid[x][y] = 1 if cmd=='on' else 0
	pass

def grid_count_on() -> int:
	cnt = 0
	for line in light_grid:
		cnt+=sum(line)
	return cnt

def solve_part_1(demo:bool) -> str:

	fn = utils.get_input_file(demo, ISSUE, True)
	print(fn)
	"""Do something here >>>"""

	# ~ parse
	instrs0 = utils.read_file_into_list(fn)
	instrs = []
	for instr in instrs0:
		il = instr.split()

		dinstr = {
			'cmd':None,
			'begin':None,
			'end':None
		}

		if il[0]=='turn':
			# ~ turn on/off
			dinstr['cmd'] = il[1]
			dinstr['begin'] = tuple(map(int,il[2].split(',')))
			dinstr['end'] = tuple(map(int,il[4].split(',')))
			pass
		else:
			# ~ toggle
			dinstr['cmd'] = il[0]
			dinstr['begin'] = tuple(map(int,il[1].split(',')))
			dinstr['end'] = tuple(map(int,il[3].split(',')))
			pass

		instrs.append(dinstr)
	print(instrs)

	# ~ apply
	for inst in instrs:
		grid_apply(dinstr['begin'], dinstr['end'], dinstr['cmd'])

	# ~ count on
	answer = grid_count_on()

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
