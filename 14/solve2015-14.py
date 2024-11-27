#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# randylampa/AoC2015
# Advent of Code 2015 - 14
# @link https://adventofcode.com/2015/day/14

import sys
import os
cur_dir = os.path.dirname(os.path.realpath(__file__))
par_dir = os.path.dirname(cur_dir)
sys.path.append(par_dir)
import utils
import re

YEAR = 2015
DAY = 14
ISSUE = '14'


def dumpDeers(deers:list):
	print('Deers:')
	for deer in deers:
		print(deer)
	return

'''
	SOLVE PART 1
'''
def solve_part_1(demo:bool) -> str:

	fn = utils.get_input_file(1 if demo else 0, DAY, YEAR)
	print(fn)
	fl = cur_dir + '/' + fn
	"""Do something here >>>"""

	simlen = 1000 if demo else 2503

	lines = utils.read_file_into_list(fn)
	print(lines)

	deers = []
	for line in lines:
		mm = re.search('^(?P<who>\w+) can fly (?P<speed>\d+) km/s for (?P<flytime>\d+) seconds, .* for (?P<resttime>\d+) seconds\.$', line)
		deer = mm.groupdict()
		print(deer)
		deer['speed'] = int(deer['speed'])
		deer['flytime'] = int(deer['flytime'])
		deer['resttime'] = int(deer['resttime'])
		deers.append(deer)
	dumpDeers(deers)

	"""simulate:"""
	maxdist = 0
	for deer in deers:
		time = deer['flytime'] + deer['resttime']
		cycles = int(simlen / time)

		realtime = cycles * time
		realdist = cycles * deer['speed'] * deer['flytime']

		# assume: (simlen - realtime) > deer['flytime'] # is wrong in realdata!

		remain_time = simlen - realtime
		remain_flytime = deer['flytime'] if remain_time > deer['flytime'] else remain_time
		realtime += remain_flytime
		realdist += deer['speed'] * remain_flytime

		deer['realdist'] = realdist
		deer['realtime'] = realtime

		maxdist = max(maxdist, realdist)
	dumpDeers(deers)

	answer = maxdist

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

	solve_part_1(0)

	# ~ solve_part_2(1)

	pass

if __name__ == '__main__':
	sys.exit(main())
