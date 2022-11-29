#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Aoc 2015 - 07

import sys
import re
sys.path.append('..')
import utils

ISSUE=7

def parse_connection(line:str) -> dict:
	conn = line.strip().split(' -> ')
	# ~ print(conn)
	wire = {
		'name': conn[1],
		'value': None,
		'gate': None,
		'inputs': [], # should be list
	}

	mm = re.search("(([a-z0-9]+) )?((NOT|OR|AND|LSHIFT|RSHIFT) )?([a-z0-9]+)", conn[0])
	gate = mm.group(4) # gate
	opL = mm.group(2) # L operand
	opR = mm.group(5) # R operand (or direct value)

	if gate:
		wire['gate'] = gate
	if opL:
		# number or wire??
		wire['inputs'].append(int(opL) if opL.isdigit() else opL)
	if opR:
		# number or wire??
		wire['inputs'].append(int(opR) if opR.isdigit() else opR)

	return wire

def print_connections(connections:list):
	print('connections>>>')
	for wire in connections:
		print(connections)
	print('<<<connections')

def print_wires(wires:list):
	print('wires>>>')
	for wire_name in wires:
		print(wire_name, wires[wire_name])
	print('<<<wires')

def clean_wires(wires:list):
	for wire_name in wires:
		wires[wire_name]['value'] = None

def get_input_value(input_element, wires:list) -> int:
	if type(input_element) is int:
		return input_element
	return evaluate_wire(input_element, wires)

def evaluate_wire(wire_name:str, wires:list) -> int:
	'''side effect!! - sets wire.value'''
	wire = wires[wire_name]
	if wire['value'] is not None:
		return wire['value']
	gate = wire['gate']
	if gate=='NOT':
		value = ~get_input_value(wire['inputs'][0], wires)
	elif gate=='OR':
		value = get_input_value(wire['inputs'][0], wires) | get_input_value(wire['inputs'][1], wires)
	elif gate=='AND':
		value = get_input_value(wire['inputs'][0], wires) & get_input_value(wire['inputs'][1], wires)
	elif gate=='LSHIFT':
		value = get_input_value(wire['inputs'][0], wires) << get_input_value(wire['inputs'][1], wires)
	elif gate=='RSHIFT':
		value = get_input_value(wire['inputs'][0], wires) >> get_input_value(wire['inputs'][1], wires)
	else:
		# is None
		value = get_input_value(wire['inputs'][0], wires)
	wire['value'] = value if value >=0 else value + 65536 # ensure positive?
	return wire['value']

def update_wires(wires:list):
	for wire_name in wires:
		evaluate_wire(wire_name, wires)

def solve_part_1(demo:bool) -> str:

	fn = utils.get_input_file(demo, ISSUE, True)
	print(fn)
	"""Do something here >>>"""

	connections = utils.read_file_into_list(fn, parse_connection)
	# ~ print_connections(connections)

	wires = {}
	for wire in connections:
		wires[wire['name']] = wire
	# ~ print_wires(wires)

	update_wires(wires)
	# ~ print_wires(wires)

# ~ # demo final values
# ~ d: 72
# ~ e: 507
# ~ f: 492
# ~ g: 114
# ~ h: 65412
# ~ i: 65079
# ~ x: 123
# ~ y: 456


	# ~ wire_in_question_name = 'g' # demo
	wire_in_question_name = 'a'
	answer = wires[wire_in_question_name]['value']

	"""<<< Do something here"""
	utils.print_answer(1, demo, answer)
	return answer

def solve_part_2(demo:bool) -> str:

	fn = utils.get_input_file(demo, ISSUE, True)
	print(fn)
	"""Do something here >>>"""

	connections = utils.read_file_into_list(fn, parse_connection)
	# ~ print_connections(connections)

	wires = {}
	for wire in connections:
		wires[wire['name']] = wire
	# ~ print_wires(wires)

	update_wires(wires)
	# ~ print_wires(wires)

	wire_a_value = wires['a']['value']
	print(['wire_a_value before', wire_a_value])

	# set 'b's new value
	wires['b']['gate'] = None
	wires['b']['inputs'] = [wire_a_value]

	# ~ print(wires['a'])
	# ~ print(wires['b'])

	clean_wires(wires)
	# ~ print(wires['a'])
	# ~ print(wires['b'])
	
	update_wires(wires)

	wire_a_value = wires['a']['value']
	print(['wire_a_value after', wire_a_value])
	
	answer = wire_a_value

	"""<<< Do something here"""
	utils.print_answer(2, demo, answer)
	return answer

def main(args):

	# ~ solve_part_1(0)

	solve_part_2(0)

	return 0

if __name__ == '__main__':
	sys.exit(main(sys.argv))
