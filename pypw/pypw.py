#!/usr/bin/python
# -*- coding: UTF-8 -*-

import sys
from random import shuffle
from random import randint
from collections import OrderedDict
from string import punctuation, lowercase

class RandomPassword:
	def __init__(self, sequence=None, mixedCases=True):
		points = {50: 'excellent', 15: 'good', 10: 'less than good', 5: 'medium', 0: 'bad'}
		self.ranking = OrderedDict(reversed(sorted(points.items())))
		self.sequence = sequence
		self.mixedCases = mixedCases
		self.phonetic_mappings = {
			'a': ['alfa', 'adam', 'arnold', 'alice'],
			'b': ['beta', 'ben', 'benjamin', 'boo'],
			'c': ['charlie', 'charles', 'charlene'],
			'd': ['delta', 'dan', 'darlene', 'dennis'],
			'e': ['echo', 'eric', 'elton', 'emma'],
			'f': ['foxtrot', 'fanny', 'fabian'],
			'g': ['golf', 'george', 'giana'],
			'h': ['hotel', 'henry', 'holly'],
			'i': ['india', 'indy', 'iris'],
			'j': ['juliett', 'james', 'john', 'jacquelyn'],
			'k': ['kilo', 'karina', 'kale'],
			'l': ['lima', 'lilly', 'lars', 'laszlo'],
			'm': ['mike', 'missy', 'marcus'],
			'n': ['november', 'noah', 'nadine'],
			'o': ['oscar', 'oda'],
			'p': ['papa', 'paul', 'pierce', 'paula'],
			'q': ['quebec', 'quang', 'quentin', 'queen'],
			'r': ['romeo', 'rachel', 'remus'],
			's': ['sierra', 'sara', 'salomon', 'sal'],
			't': ['tango', 'tim', 'timothy', 'tanya'],
			'u': ['uniform', 'ulrik', 'uma'],
			'v': ['victor', 'vic', 'victoria', 'valery'],
			'w': ['whiskey', 'walter', 'walt', 'wilma', 'wonda'],
			'x': ['xray', 'xenia', 'xander'],
			'y': ['yankee', 'yolanda', 'yoav', 'yosef'],
			'z': ['zulu', 'zach', 'zarah'],
		}
		self.possible_alpha = lowercase
		self.possible_num = [str(i) for i in xrange(0, 9)]
		self.possible_meta = punctuation


	def randomBool(self):
		return randint(0, 1) is 1


	def randCase(self, sequence):
		return [c.upper() if self.randomBool() and c.isalnum() else c.lower() for c in sequence]


	def generateRandomPW(self, length=None, alpha=True, digits=True, symbols=True):
		if length is None:
			length = 12

		sequence = list()
		params = 0

		if alpha:
			params += 1
		if digits:
			params += 1
		if symbols:
			params += 1

		try:
			divider = length / params
		except ZeroDivisionError:
			print 'ERROR: Cannot divide by 0, provide atleast one of either alpha, digits or symbols.'
			sys.exit(0)

		if alpha:
			counter = 0
			while counter <= divider:
				sequence.append(self.possible_alpha[randint(0, len(self.possible_alpha) - 1)])
				counter += 1

		if digits:
			counter = 0
			while counter <= divider:
				sequence.append(self.possible_num[randint(0, len(self.possible_num) - 1)])
				counter += 1

		if symbols:
			counter = 0
			while counter <= divider:
				sequence.append(self.possible_meta[randint(0, len(self.possible_meta) - 1)])
				counter += 1

		shuffle(sequence)
		if self.mixedCases:
			result = ''.join(self.randCase(sequence))
		else:
			result = ''.join(sequence)
		strength = self.strength(result)
		phonetic = self.phonetic(result)
		return {'string': result, 'ranking': strength[0], 'score': strength[1], 'phonetic': phonetic}		


	def generatePW(self):
		salt = [c for c in self.sequence]
		shuffle(salt)
		if self.mixedCases:
			result = ''.join(self.randCase(salt))
		else:
			result = ''.join(salt)
		strength = self.strength(result)
		phonetic = self.phonetic(result)
		return {'string': result, 'ranking': strength[0], 'score': strength[1], 'phonetic': phonetic}


	def phonetic(self, sequence):
		result = ''
		for c in sequence:
			if c.isalpha() and c.lower() in self.phonetic_mappings:
				possibilities = self.phonetic_mappings[c.lower()]
				result += possibilities[randint(0, len(possibilities) - 1)] + ' '
			else:
				result += c + ' '
		return result


	def strength(self, sequence):
		chart = {'length': 0, 'numbers': 0, 'symbols': 0, 'casing': 0}
		length = len(sequence)
		if length >= 8:
			chart['length'] += 10 + length - 8
		for c in sequence:
			if not c.isalnum():
				chart['symbols'] += 1
			else:
				if c.isdigit():
					chart['numbers'] += 1
				if c.istitle():
					chart['casing'] += 1
		chart['sum'] = chart['length'] + chart['numbers'] + chart['symbols'] + chart['casing']
		for key, value in self.ranking.items():
			if chart['sum'] > key:
				return value, chart['sum']


def main():
	import argparse

	parser = argparse.ArgumentParser(description='Generate random Password')
	parser.add_argument('-s', '--sequence', type=str, help='The sequence to generate the random string from. Enclose the string in double quotes if it contains non-alphanumeric characters', required=False)
	parser.add_argument('--mixed', dest='mixed', action='store_true', help='Generate random casing', required=False)
	parser.add_argument('--not-mixed', dest='mixed', action='store_false', help='Do NOT generate random casing', required=False)
	parser.add_argument('-l', '--length', type=int, help='Generate a random password with l-length. Default: 12')
	parser.add_argument('--no-digits', dest='digits', action='store_false', help='Do not use digits in random password')
	parser.add_argument('--no-letters', dest='letters', action='store_false', help='Do not use alphabetical letters in random password')
	parser.add_argument('--no-symbols', dest='symbols', action='store_false', help='Do not use symbols in random password')
	parser.set_defaults(mixed=True)
	parser.set_defaults(digits=True)
	parser.set_defaults(letters=True)
	parser.set_defaults(symbols=True)

	args = vars(parser.parse_args())

	sequence = args['sequence']
	mixed = args['mixed']
	randomLength = args['length']
	digits = args['digits']
	alpha = args['letters']
	symbols = args['symbols']

	if sequence is not None:
		pw = RandomPassword(sequence, mixedCases=mixed)
		result = pw.generatePW()
	else:
		pw = RandomPassword()
		result = pw.generateRandomPW(length=randomLength, alpha=alpha, digits=digits, symbols=symbols)
	for k, v in result.items():
		print '%s: %s' % (k, v)


if __name__=='__main__':
	main()
