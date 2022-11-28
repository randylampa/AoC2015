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

def word_is_nice2(word:str) -> bool:
	word = word.strip()
	wl = len(word)
	# ~ print("Word `{}`".format(word))
	hasDoubles = False
	hasCyclope = False

	# search for cyclopes (najit kyklopa jejednodussi - jeden linearni cyklus)
	i = 0
	while i < wl-2:
		cl = word[i]
		cr = word[i+2]
		# ~ print("compare cyclope `{}_{}`".format(cl,cr))
		if cl==cr:
			hasCyclope = True
			# ~ print("found cyclope `{}` on position {}".format(cl, i))
			break
		i+=1
	if not hasCyclope:
		# ~ print("Word `{}` does not contain cyclope".format(word))
		return False

	# search for doubles
	j = 0
	while j < wl-2:
		double = word[j:j+2]
		i = j+1 # ensure no overlap
		while i < wl-2:
			i+=1
			double2 = word[i:i+2]
			# ~ print("compare double `{}` to `{}`".format(double, double2))
			if double == double2:
				hasDoubles = True
				# ~ print("found double `{}` on position {} and {}".format(double, j, i))
				i=j=wl # cause break of both cycles
				break
		j+=1
	if not hasDoubles:
		# ~ print("Word `{}` does not contain doubles".format(word))
		return False

	return hasDoubles and hasCyclope

def solve_part_2(demo:bool) -> str:

	fn = utils.get_input_file(demo, ISSUE, True)
	print(fn)
	"""Do something here >>>"""

	words_are_nice = utils.read_file_into_list(fn, word_is_nice2)
	# ~ print(words_are_nice)

	answer = sum(words_are_nice)

	"""<<< Do something here"""
	utils.print_answer(2, demo, answer)
	return answer

def main(args):

	#solve_part_1(0)

	solve_part_2(0)

	return 0

if __name__ == '__main__':
	sys.exit(main(sys.argv))
