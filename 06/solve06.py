#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Aoc 2015 - 06

import sys
sys.path.append('..')
import utils

ISSUE=6

gridsize = 1000
#~ gridsize = 10

def parse_instructions(lines:list) -> list:
	dinstrs = []
	for line in lines:
		il = line.split()

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
		# TODO: test gridsize limits
		dinstrs.append(dinstr)
	return dinstrs

def init_grid(gridsize:int, default_value:int = 0):
	#~ return [[default_value] * gridsize] * gridsize # TOTO NEJEDE! (dělá duplikáty objektů)
	return [[default_value for x in range(gridsize)] for x in range(gridsize)]

def print_grid(light_grid:list):
	#~ print("light_grid")
	#~ print(light_grid)
	for line in light_grid:
		print(line)

def grid_apply(light_grid:list, begin:tuple, end:tuple, cmd:str):
	#~ print("grid_apply", (cmd, begin, end))
	for y in range(begin[1], end[1] + 1):
		for x in range(begin[0], end[0] + 1):
			val = light_grid[y][x]
			if cmd == 'toggle':
				val2 = 0 if val==1 else 1
			else:
				val2 = 1 if cmd=='on' else 0
			#~ print((x,y,cmd,val,val2))
			light_grid[y][x] = val2
	#~ print_grid(light_grid)
	#~ print(light_grid)

def grid_count_on(light_grid:list) -> int:
	cnt = 0
	for line in light_grid:
		cnt+=sum(line)
	return cnt

def solve_part_1(demo:bool) -> str:

	fn = utils.get_input_file(demo, ISSUE, True)
	#~ fn+='a';
	print(fn)
	"""Do something here >>>"""

	light_grid = init_grid(gridsize)
	#~ print_grid(light_grid)

	# ~ parse
	dinstrs = parse_instructions(utils.read_file_into_list(fn))
	#~ print(dinstrs)

	# ~ apply
	for dinstr in dinstrs:
		grid_apply(light_grid, dinstr['begin'], dinstr['end'], dinstr['cmd'])

	#~ print_grid(light_grid)

	# ~ count on
	answer = grid_count_on(light_grid)

	"""<<< Do something here"""
	utils.print_answer(1, demo, answer)
	return answer

def solve_part_2(demo:bool) -> str:

	fn = utils.get_input_file(demo, ISSUE, True)
	print(fn)
	"""Do something here >>>"""

	light_grid = init_grid(gridsize)
	#~ print_grid(light_grid)

	# ~ parse
	dinstrs = parse_instructions(utils.read_file_into_list(fn))
	#~ print(dinstrs)

	# ~ apply
	for dinstr in dinstrs:
		grid_apply(light_grid, dinstr['begin'], dinstr['end'], dinstr['cmd'])

	# ~ count on
	answer = grid_count_on(light_grid)

	"""<<< Do something here"""
	utils.print_answer(2, demo, answer)
	return answer

def main(args):

	solve_part_1(0)

	# ~ solve_part_2(1)

	return 0

if __name__ == '__main__':
	sys.exit(main(sys.argv))
