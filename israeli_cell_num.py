#!/usr/bin/env python

import re

def normalize(num):
	"""Normalize a Israeli cell number to a standard international form,
	+972-PP-XXXX-XXX, Where PP is the Carier prefix.
	
	# Accepted input (9 digits, possible extra leading zero)
	>>> print normalize('055-6677889')
	+972-55-667-7889

	>>> print normalize('0556677889')
	+972-55-667-7889

	>>> print normalize('556677889')
	+972-55-667-7889

	>>> print normalize('+972-556677889')
	+972-55-667-7889

	>>> print normalize('5-5-6-6-7-7-8-8-9')
	+972-55-667-7889

	# Erroneous input
	>>> print normalize('X')
	None

	>>> print normalize('556677')
	None

	"""
	try:
		digits=''.join(re.findall('\d', num))
		if digits[0]=='0':				# Optional leading zero
			digits=digits[1:]
		if digits.startswith('972'):	# Internationl prefix
			digits=digits[3:]
		if len(digits)!=9:
			return None
		return "+972-"+digits[0:2]+"-"+digits[2:5]+"-"+digits[5:9]
	except:
		return None
	
		
if __name__ == "__main__":
	import doctest
	doctest.testmod(verbose=True)
