#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# randylampa/AoC2015
# Advent of Code 2015 - 15
# @link https://adventofcode.com/2015/day/15

import sys
import os
cur_dir = os.path.dirname(os.path.realpath(__file__))
par_dir = os.path.dirname(cur_dir)
sys.path.append(par_dir)
import utils
import re
import math

YEAR = 2015
DAY = 15
ISSUE = '15'

if sys.version_info < (3,8):
	"""https://docs.python.org/3/library/math.html#math.prod"""
	exit("requires  Py-ver>=3.8, 'cos using `math.prod`")


def gen_con2(total:int = 100)->tuple:
	for i in range(total):
		if i==0: continue
		jmax = total-i
		yield (i,jmax)

def gen_con3(total:int = 100)->tuple:
	for i in range(total):
		if i==0: continue
		jmax = total-i
		for j in range(jmax):
			if j==0: continue
			kmax = jmax-j
			yield (i,j,kmax)

def gen_con4(total:int = 100)->tuple:
	for i in range(total):
		if i==0: continue
		jmax = total-i
		for j in range(jmax):
			if j==0: continue
			kmax = jmax-j
			for k in range(kmax):
				if k == 0: continue
				lmax = kmax-k
				yield (i,j,k,lmax)


def parseIngredients(demo:bool)->list:
	fn = utils.get_input_file(1 if demo else 0, DAY, YEAR)
	print(fn)
	fl = cur_dir + '/' + fn

	lines = utils.read_file_into_list(fn)
	# ~ print(lines)

	ingrts = []
	for line in lines:
		mm = re.search('^(?P<name>\w+): capacity (?P<cap>-?\d+), durability (?P<dur>-?\d+), flavor (?P<fla>-?\d+), texture (?P<tex>-?\d+), calories (?P<cal>-?\d+)$', line)
		ingrt = mm.groupdict()
		# ~ print(ingrt)
		ingrt['cap'] = int(ingrt['cap'])
		ingrt['dur'] = int(ingrt['dur'])
		ingrt['fla'] = int(ingrt['fla'])
		ingrt['tex'] = int(ingrt['tex'])
		ingrt['cal'] = int(ingrt['cal'])
		# ~ print(ingrt)
		ingrts.append(ingrt)
	return ingrts

def dumpMixtures(mixtures:list):
	for mix in mixtures:
		print(mix)

'''
	SOLVE PART 1
'''
def solve_part_1(demo:bool) -> str:

	ingrts = parseIngredients(demo)
	print(ingrts)
	"""Do something here >>>"""

	ningr = len(ingrts)
	if ningr == 2:
		gen_con = gen_con2
	elif ningr == 3:
		gen_con = gen_con3
	elif ningr == 4:
		gen_con = gen_con4
	else:
		exit("generator not defined for {} ingredients".format(ningr))

	mixtures = []
	mixture_values = []
	for q in gen_con(100):
		# ~ print("testing concentration:", q)
		mixture = {
			'cap': 0,
			'dur': 0,
			'fla': 0,
			'tex': 0,
		}
		for i in range(ningr):
			spoons = q[i]
			ingrt = ingrts[i]
			# ~ print("take {} spoon(s) of {}".format(spoons, ingrt['name']))
			mixture['cap'] += spoons * ingrt['cap']
			mixture['dur'] += spoons * ingrt['dur']
			mixture['fla'] += spoons * ingrt['fla']
			mixture['tex'] += spoons * ingrt['tex']
		# ~ print(mixture)
		mv = mixture.values()
		if min(mv) < 1:
			# ~ print("disqualify mixture as non-positive: ", mixture)
			continue
		value = math.prod(mv)
		mixture['value'] = value
		mixture_values.append(value)

		# ~ mixture['concentrations'] = q # WHY? THIS IS KILLING EXECUTION - CPU&MEM 100%

		mixtures.append(mixture)

		# ~ exit('ll')
	dumpMixtures(mixtures)
	# ~ print(mixture_values)

	answer = max(mixture_values)

	"""<<< Do something here"""
	utils.print_answer(1, demo, answer)
	return answer


'''
	SOLVE PART 2
'''
def solve_part_2(demo:bool) -> str:

	ingrts = parseIngredients(demo)
	print(ingrts)
	"""Do something here >>>"""

	ningr = len(ingrts)
	if ningr == 2:
		gen_con = gen_con2
	elif ningr == 3:
		gen_con = gen_con3
	elif ningr == 4:
		gen_con = gen_con4
	else:
		exit("generator not defined for {} ingredients".format(ningr))

	mixtures = []
	mixture_values = []
	for q in gen_con(100):
		# ~ print("testing concentration:", q)
		mixture = {
			'cap': 0,
			'dur': 0,
			'fla': 0,
			'tex': 0,
			'cal': 0,
		}
		for i in range(ningr):
			spoons = q[i]
			ingrt = ingrts[i]
			# ~ print("take {} spoon(s) of {}".format(spoons, ingrt['name']))
			mixture['cap'] += spoons * ingrt['cap']
			mixture['dur'] += spoons * ingrt['dur']
			mixture['fla'] += spoons * ingrt['fla']
			mixture['tex'] += spoons * ingrt['tex']
			mixture['cal'] += spoons * ingrt['cal']
		# ~ print(mixture)
		mv = list(mixture.values())[:-1] # do not count 'cal' to total score
		value = math.prod(mv)

		mixture['value'] = value
		mixture['concs'] = q

		if min(mv) < 1:
			# ~ print("disqualify mixture as non-positive:", mixture)
			continue
		if mixture['cal'] != 500:
			# ~ print("disqualify mixture due to calories requirements:", mixture)
			continue

		mixture_values.append(value)
		mixtures.append(mixture)
	dumpMixtures(mixtures)
	# ~ print(mixture_values)

	answer = max(mixture_values)

	"""<<< Do something here"""
	utils.print_answer(2, demo, answer)
	return answer

def main():

	# ~ solve_part_1(0)

	solve_part_2(0)

	pass

if __name__ == '__main__':
	sys.exit(main())
