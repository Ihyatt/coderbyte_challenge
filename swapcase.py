import string
def swap_case(strin):
	"""take the str parameter and swap the case of each character. 
	For example: if str is "Hello World" the output should be hELLO wORLD. 
	Let numbers and symbols stay the way they are. 
	Example::
	>>> swap_case("Hello-LOL")
	'hELLO-lol'
	>>> swap_case("Sup DUDE!!?")
	'sUP dude!!?'
	"""
	swapped = ""

	alpha_lower = list(string.ascii_lowercase)
	alpha_upper = list(string.ascii_uppercase)

	for letter in strin:
		if letter in alpha_lower:
			swapped += letter.upper()
		elif letter in alpha_upper:
			swapped += letter.lower()
		else:
			swapped += letter

	return swapped

#####################################################################
if __name__ == "__main__":
	print
	import doctest
	if doctest.testmod().failed == 0:
		print "*** ALL TESTS PASSED ***"	
