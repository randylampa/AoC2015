#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Aoc 2015 - 09

import sys
import re
sys.path.append('..')
import utils

ISSUE=9

def parse_line(line:str) -> dict:
	mm = re.search("(?P<A>\w+) to (?P<B>\w+) = (?P<dist>\d+)", line)
	dm = mm.groupdict()
	dm['dist'] = int(dm['dist'])
	# ~ print(dm)
	return dm
	# ~ return (mm.group(1), mm.group(2), int(mm.group(3)))

def build_city_map(inputs:list) -> dict:
	city_map = {}
	for inp in inputs:
		nA = inp['A']
		nB = inp['B']
		if nA not in city_map:
			city_map[nA] = {}
		if nB not in city_map:
			city_map[nB] = {}
		dA = city_map[nA]
		dB = city_map[nB]
		dA[nB] = inp['dist']
		dB[nA] = inp['dist']
		# ~ print('ooj', dA, dB)
	# ~ print(city_map)
	return city_map

def print_city_map(city_map:dict):
	for city in city_map.items():
		print(city[0])
		for nexts in city[1].items():
			print("\t{}\tto {}".format(nexts[1], nexts[0]))

def find_shortest_step(city:dict, avoid:set = {}) -> tuple:
	shortest = None
	for item in city.items():
		# ~ print(item)
		if (shortest is None or item[1] < shortest[1]) and item[0] not in avoid:
			shortest = item
	return shortest

def walk_shortest(city_map:dict, start:str) -> tuple:
	'''
	return: (path_cities, path_distances)
	'''
	path_cities = [start]
	path_distances = []
	while True:
		ss = find_shortest_step(city_map[path_cities[-1]], set(path_cities))
		# ~ print('ss', start, ss)
		if ss is None:
			break
		else:
			path_cities.append(ss[0])
			path_distances.append(ss[1])
	# ~ print(path_cities, path_distances)
	return (path_cities, path_distances)

'''
	SOLVE PART 1
'''
def solve_part_1(demo:bool) -> str:

	fn = utils.get_input_file(demo, ISSUE, True)
	print(fn)
	"""Do something here >>>"""

	inputs = utils.read_file_into_list(fn, parse_line)
	# ~ print(inputs)

	city_map = build_city_map(inputs)
	# ~ print(city_map)
	print_city_map(city_map)

	start = list(city_map.keys())[0] # select first city as start
	shortest_route = walk_shortest(city_map, start)
	print(shortest_route)
	path_cities, path_distances = shortest_route

	answer = sum(path_distances)

	"""<<< Do something here"""
	utils.print_answer(1, demo, answer)
	return answer

def find_longest_step(city:dict, avoid:set = {}) -> tuple:
	longest = None
	for item in city.items():
		# ~ print(item)
		if (longest is None or item[1] > longest[1]) and item[0] not in avoid:
			longest = item
	return longest

def walk_longest(city_map:dict, start:str) -> tuple:
	'''
	return: (path_cities, path_distances)
	'''
	path_cities = [start]
	path_distances = []
	while True:
		ss = find_longest_step(city_map[path_cities[-1]], set(path_cities))
		# ~ print('ss', start, ss)
		if ss is None:
			break
		else:
			path_cities.append(ss[0])
			path_distances.append(ss[1])
	# ~ print(path_cities, path_distances)
	return (path_cities, path_distances)

'''
	SOLVE PART 2
'''
def solve_part_2(demo:bool) -> str:
	fn = utils.get_input_file(demo, ISSUE, True)
	print(fn)
	"""Do something here >>>"""

	inputs = utils.read_file_into_list(fn, parse_line)
	# ~ print(inputs)

	city_map = build_city_map(inputs)
	# ~ print(city_map)
	print_city_map(city_map)

	# to overcome inconsistency... try start at all cities and compare routes.. i know, it's a little brute but anyway
	longest = None
	for start in list(city_map.keys()):
		path_cities, path_distances = walk_longest(city_map, start)
		length = sum(path_distances);
		print("Start at `{}` is {} long".format(start, length))
		print("\t", path_cities, path_distances)
		if longest is None or length > longest[1]:
			longest = (start, length)

	answer = longest[1]

	"""<<< Do something here"""
	utils.print_answer(2, demo, answer)
	return answer

def main(args):

	solve_part_1(0)
	# demo: 605
	# hot: 141 (inconsistent between runs.. how?)
	# ['Arbre', 'Tambi', 'Snowdin', 'Faerun', 'Straylight', 'Norrath', 'AlphaCentauri', 'Tristram'], [40, 22, 12, 21, 9, 34, 3]
	'''
	rozdíl je v tom, kde se začne. ke konzistentnímu získání nejkratší
	cesty je potřeba uzavřít kruh (vrátit se na start) a potom najít
	nejdelší krok a tady cyklus rozdělit (tam kde je nejdelší spojnice
	bude začátek a konec)(tudy nepůjdu)
	'''

	# ~ solve_part_2(0)

	return 0

"""
	Další možnost řešení:_
	Sestavit list dvojic s nejkratšími vzdálenostmi. V druhém listu by byly délky mezi nimi (na stejném indexu)
	city[0] = {'AlphaCentauri', 'Tristram'}
	dist[0] = 3
	-
	city[1] = {'Snowdin', 'Faerun'}
	dist[1] = 12
	-
	...
	Najdu v seznamu nejdelší vzdálenost, a to bude start/cíl (najdu na stejném indexu).
	Potom si jeden prvek vyberu a budu procházet indexy a hledat ve kterém setu se nachází.
	když najdu, vezmu druhý ze setu a pokračuju. Kvuli zefektivnení procházení mám nekonečný
	cyklus, který rotuje indexy (zalomí na začátek) a udržuju si start/cíl, aktuálně hledaný prvek a
	pozice které již testovat nemám (set indexů kde se něco dělo) `if i in indices continue`.

	Proces končí, pokud délka vyloučených indexů je rovna počtu záznamů nebo následující město které mám hledat se nachází v setu start/cíl. resp v proměnné konec

	SHIT!!!
	Strašně závisí na tom, aby v seznamu existovala cesta...
"""
def naive():
	city = [
		{'AlphaCentauri', 'Tristram'},
		{'Snowdin', 'Faerun'},
		{'Tambi', 'Tristram'},
		{'Faerun', 'Straylight'},
		{'Norrath', 'Straylight'},
		{'Straylight', 'Tristram'},
		{'Tristram', 'Arbre'}
	]
	dist = [
		3,
		12,
		35,
		21,
		9,
		27,
		90,
	]
	idx_start_fin = dist.index(max(dist)) # max if in search for shortest..
	idx_avoid = {idx_start_fin}
	city_start, city_end = city[idx_start_fin]
	print("Find path from {} to {}".format(city_start, city_end))
	city_find = city_start
	idx = -1
	cnt = len(city)
	pathlens = []
	cnt_iter = 0
	while True:
		cnt_iter+=1
		idx+=1
		if idx>=cnt:
			idx=0 # wrap index
		# ~ if True:
			# ~ print('DBG idx', idx)
			# ~ continue
		if idx in idx_avoid:
			continue # skip some indices
		print('DBG find', city_find, idx, city[idx])
		if city_find in city[idx]:
			pathlens.append(dist[idx])
			idx_avoid.add(idx) # add to skip this index
			x = city[idx].copy() # make copy to not interfere with original data
			x.discard(city_find) # remove found city
			city_find = tuple(x)[0] # take next city from found set
			print('city_find', city_find, idx_avoid)
		if city_find == city_end:
			break # we come to an end
		if len(idx_avoid)>=cnt or cnt_iter>=cnt**2:
			print('HALT - unexpected...', cnt_iter, idx_avoid)
			break # we visited all, just for security
		pass
	print("Path from {} to {} is {} long and takes these steps".format(city_start, city_end, sum(pathlens)), pathlens)
	pass

if __name__ == '__main__':
	# ~ sys.exit(main(sys.argv))
	naive()
