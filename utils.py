#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Aoc 2015
#

import sys
import re


def get_input_file(demo, issue: int = None, sensible: bool = False) -> str:
	s = str(issue).rjust(2, '0') if issue is not None else ''
	f = 'input{}' if not demo else 'input{}-demo' if not sensible else 'input-demo{}'
	return f.format(s)


def get_output_file(demo, issue: int = None, sensible: bool = False) -> str:
	s = str(issue).rjust(2, '0') if issue is not None else ''
	f = 'output{}' if not demo else 'output{}-demo' if not sensible else 'output-demo{}'
	return f.format(s)


def read_file_into_lines(name: str = 'input', mode: str = 'r') -> list:
	"""
	eads all lines into list
	"""
	f = open(name, 'r')
	lines = f.readlines()
	f.close()
	return lines


def read_file_into_list(name='input', mapfnc=lambda x: x.strip()) -> list:
	"""
	Reads all lines into list and map mapfnc on each.
	"""
	return [*map(mapfnc, read_file_into_lines(name))]


def read_file_into_list_bin(name='input', mapfnc=None) -> list:
	"""
	Reads all lines into list and map mapfnc on each.
	"""
	lines = read_file_into_lines(name, 'rb')
	if mapfnc is not None:
		return [*map(mapfnc, lines)]
	else:
		return lines


def read_file_into_list_of_ints(name='input') -> list:
	"""
	Reads all lines into list and map int(x.strip()) on each.
	"""
	return read_file_into_list(name, lambda x: int(x.strip()))


def read_file_into_lists_of_ints(name='input') -> list:
	"""
	Read all lines into list of lists (sep=,)
	"""
	return read_file_into_list(name, lambda x: [*map(int, x.strip().split(','))])


def read_file_into_dict(name: str = 'input', kvpattrn: str='(?P<k>.*):\s*(?P<v>.*)', vmap=int) -> dict:
	"""
	Reads all lines into dict and maps vmap on each value
	"""
	outdict = {}
	for line in read_file_into_lines(name):
		mm = re.search(kvpattrn, line)
		k = mm.groupdict()['k']
		v = mm.groupdict()['v']
		outdict[k] = vmap(v)
	return outdict


def dump_list_of(xlist: list):
	for x in xlist:
		print(x)


def print_answer(part: int, demo, answer) -> None:
	print("Answer_{} = {}{}".format(part, answer, ' (demo)' if demo else ''))


def main(args):
	return 0


if __name__ == '__main__':
	sys.exit(main(sys.argv))
