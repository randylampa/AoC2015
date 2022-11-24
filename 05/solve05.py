#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Aoc 2015 - 05

import sys
sys.path.append('..')
import utils

ISSUE=5

def word_is_nice(word:str) -> bool:
	
	has_three_vowels = False
	has_doubleletter = False
	has_restricted = False
	
	# search for restricted
	restricted = ['ab','cd','pq','xy']
	for rs in restricted:
		if word.find(rs) > -1:
			#~ print("Word `{}` contains restricted substring `{}`".format(word, rs))
			has_restricted = True
			break # shortcut

	if has_restricted:
		#~ print("Word `{}` contains restricted substring".format(word))
		return False # shortcut
		pass

	# search vowels
	vowel_count = 0
	vowels = "aeiou"
	for letter in word:
		if vowels.find(letter) > -1:
			#~ print("Word `{}` contains vowel `{}`".format(word, letter))
			vowel_count+=1
	if vowel_count>=3:
		has_three_vowels = True
	else:
		#~ print("Word `{}` does not contain 3 vowels".format(word))
		return False # shortcut
		pass

	# search doubles
	prev_letter = None
	for letter in word:
		if prev_letter is not None and letter == prev_letter:
			#~ print("Word `{}` contains double letter `{}`".format(word, letter))
			has_doubleletter = True
			break # shortcut
		prev_letter = letter

	if not has_doubleletter:
		#~ print("Word `{}` does not contain double letter".format(word))
		return False # shortcut
		pass

	# evaluate (if no shortcut is used)
	return has_three_vowels and has_doubleletter and not has_restricted
	return True

def solve_part_1(demo:bool) -> str:

	fn = utils.get_input_file(demo, ISSUE, True)
	print(fn)
	"""Do something here >>>"""

	words = utils.read_file_into_list(fn)
	print(words)

	count_nice = 0
	for word in words:
		nice = word_is_nice(word)
		print("Word `{}` is {}".format(word, 'nice' if nice else 'naughty'))
		if nice:
			count_nice+=1
	
	answer = count_nice

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
	
	solve_part_1(0)
	
	#solve_part_2(1)
	
	return 0

if __name__ == '__main__':
	sys.exit(main(sys.argv))
