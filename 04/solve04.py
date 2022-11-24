#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Aoc 2015 - 04

import sys
import hashlib
sys.path.append('..')
import utils

ISSUE=4

INPUT_DEMO1="abcdef"
INPUT_DEMO2="pqrstuv"
INPUT="yzbqklnj"

def get_input(demo:bool=False)->str:
	if not demo:
		return INPUT
	else:
		return INPUT_DEMO1
		return INPUT_DEMO2

def solve_part_1(demo:bool) -> str:

	inp = get_input(demo)
	print('inp = `{}`'.format(inp))
	"""Do something here >>>"""

	end = False
	num = 0
	while True:
		coin = inp + str(num)
		#print(coin)
		coinhash = hashlib.md5(coin.encode()).hexdigest()
		#print(coinhash)
		if coinhash.startswith('00000'): # five zeroes
			print("Found hash {} for coin {} number {}".format(coinhash, coin, num))
			break
		num+=1
		if num>10:
			#break # only for testing
			pass
	
	answer = num

	"""<<< Do something here"""
	utils.print_answer(1, demo, answer)

	return answer

def solve_part_2(demo:bool) -> str:

	inp = get_input(demo)
	print('inp = `{}`'.format(inp))
	"""Do something here >>>"""

	end = False
	num = 0
	while True:
		coin = inp + str(num)
		#print(coin)
		coinhash = hashlib.md5(coin.encode()).hexdigest()
		#print(coinhash)
		if coinhash.startswith('000000'): # six zeroes
			print("Found hash {} for coin {} number {}".format(coinhash, coin, num))
			break
		num+=1
		if num>10:
			#break # only for testing
			pass
	
	answer = num

	"""<<< Do something here"""
	utils.print_answer(2, demo, answer)

	return answer

def main(args):

	solve_part_1(0)

	solve_part_2(0)
	
	return 0

if __name__ == '__main__':
	sys.exit(main(sys.argv))
