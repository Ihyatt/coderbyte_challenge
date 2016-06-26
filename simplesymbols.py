def simple_symbols(str):
	"""The str parameter will be composed of + and = symbols with several letters 
	between them (ie. ++d+===+c++==a) and for the string 
	to be true each letter must be surrounded by a + symbol. So the string to 
	the left would be false.
	Example::

	>>> simple_symbols("+d+=3=+s+")
	True

	>>> simple_symbols("f++d+")
	False
	"""


	letters_symbols = list(str)
	if letters_symbols[0].isalpha():
		return False
	if letters_symbols[-1].isalpha():
		return False

	idx = 1
	while idx < len(letters_symbols) - 1:
		if letters_symbols[idx].isalpha():
			if letters_symbols[idx - 1] == "+" and letters_symbols[idx + 1] == "+":
				return True
	return False




#####################################################################
if __name__ == "__main__":
	print
	import doctest
	if doctest.testmod().failed == 0:
		print "*** ALL TESTS PASSED ***"
   