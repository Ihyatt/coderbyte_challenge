def alphabet_soup(str):
	"""take the str string parameter being passed and return the string with the letters in alphabetical order 
	(ie. hello becomes ehllo). Assume numbers and punctuation symbols will not be included in the string.
	Example::
	>>> alphabet_soup('coderbyte')
	'bcdeeorty'
	>>> alphabet_soup('hooplah')
	'ahhloop'

	"""
	alpha_str = "".join(sorted(str))

	return alpha_str

#####################################################################
if __name__ == "__main__":
	print
	import doctest
	if doctest.testmod().failed == 0:
		print "*** ALL TESTS PASSED ***"