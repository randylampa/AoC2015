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


def parseDeers(demo:bool)->list:
	fn = utils.get_input_file(1 if demo else 0, DAY, YEAR)
	print(fn)
	fl = cur_dir + '/' + fn

	lines = utils.read_file_into_list(fn)
	# ~ print(lines)

	deers = []
	for line in lines:
		mm = re.search('^(?P<name>\w+) can fly (?P<speed>\d+) km/s for (?P<fly>\d+) seconds, .* for (?P<rest>\d+) seconds\.$', line)
		deer = mm.groupdict()
		# ~ print(deer)
		deer['speed'] = int(deer['speed'])
		deer['fly'] = int(deer['fly'])
		deer['rest'] = int(deer['rest'])
		deers.append(deer)
	return deers

def dumpDeers(deers:list):
	print('Deers:')
	for deer in deers:
		print(deer)
	return

'''
	SOLVE PART 1
'''
def solve_part_1(demo:bool) -> str:

	"""Do something here >>>"""

	simlen = 1000 if demo else 2503

	deers = parseDeers(demo)
	dumpDeers(deers)

	"""simulate:"""
	maxdist = 0
	for deer in deers:
		time = deer['fly'] + deer['rest']
		cycles = int(simlen / time)

		realtime = cycles * time
		realdist = cycles * deer['speed'] * deer['fly']

		# assume: (simlen - realtime) > deer['fly'] # is wrong in realdata!

		remain_time = simlen - realtime
		remain_flytime = deer['fly'] if remain_time > deer['fly'] else remain_time
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


S_FLY = 'flying'
S_REST = 'resting'

def makeStep(deer:dict)->int:
	deer['time'] += 1
	deer['instate'] += 1
	if deer['state'] == S_FLY:
		deer['dist'] += deer['speed']
		if deer['instate'] >= deer['fly']:
			deer['state'] = S_REST
			deer['instate'] = 0
	elif deer['state'] == S_REST:
		if deer['instate'] >= deer['rest']:
			deer['state'] = S_FLY
			deer['instate'] = 0
	# ~ print(deer)
	return deer['dist']

'''
	SOLVE PART 2
'''
def solve_part_2(demo:bool) -> str:

	"""Do something here >>>"""

	simlen = 1000 if demo else 2503

	deers = parseDeers(demo)
	# ~ dumpDeers(deers)

	""" init deers """
	for deer in deers:
		deer['dist'] = 0
		deer['time'] = 0
		deer['state'] = S_FLY
		deer['instate'] = 0
		deer['points'] = 0
	# ~ dumpDeers(deers)

	"""simulate:"""
	print("SIMLEN:", simlen)

	for sec in range(simlen):
		dists = []
		for deer in deers:
			dists.append(makeStep(deer))
		maxdist = max(dists)
		for deer in deers:
			if deer['dist'] == maxdist:
				deer['points'] += 1
	dumpDeers(deers)

	points = []
	for deer in deers:
		points.append(deer['points'])

	answer = max(points)

	"""<<< Do something here"""
	utils.print_answer(2, demo, answer)
	return answer

def main():

	# ~ solve_part_1(0)

	solve_part_2(0)

	pass

if __name__ == '__main__':
	sys.exit(main())
