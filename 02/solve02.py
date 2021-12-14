#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Aoc 2015 - 02

import sys
sys.path.append('..')
import utils

ISSUE=2

def read_file_into_packages(fn:str)->list:
	packages = utils.read_file_into_list(fn, lambda x:tuple(map(int,x.strip().split('x'))))
	#~ print(packages)
	return packages

def get_package_unique_areas(package:tuple)->list:
	return [
		package[0]*package[1],
		package[1]*package[2],
		package[2]*package[0]
	]

def solve_part_1():
	demo = 0

	fn = utils.get_input_file(demo, ISSUE);
	print(fn)
	"""Do something here >>>"""
	packages = read_file_into_packages(fn)
	#~ print(packages)

	paper_area = 0
	for package in packages:
		#~ print(package)
		areas = get_package_unique_areas(package)
		#~ print(areas)
		total_area = sum(list(map(lambda x:2*x,areas))) + min(areas)
		#~ print(total_area)
		paper_area+=total_area

	answer = paper_area

	"""<<< Do something here"""
	utils.print_answer(1, demo, answer)

def solve_part_2():
	demo = 1

	fn = utils.get_input_file(demo, ISSUE);
	print(fn)
	"""Do something here >>>"""

	print('Part 2 not solved yet')
	
	answer = None

	"""<<< Do something here"""
	utils.print_answer(2, demo, answer)

def main(args):
	
	solve_part_1()
	
	#~ solve_part_2()
	
	return 0

if __name__ == '__main__':
	sys.exit(main(sys.argv))
