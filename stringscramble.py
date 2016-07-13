def string_scramble(astring,bstring):
	""" have the function StringScramble(str1,str2) take both parameters
	being passed and return the string true if a portion of str1 characters 
	can be rearranged to match str2, otherwise return the string false. For 
	example: if str1 is "rkqodlw" and str2 is "world" the output should return 
	true. Punctuation and symbols will not be entered with the parameters. 
	Example::
	>>> string_scramble("cdore","coder")
	True
	>>> string_scramble("h3llko", "hello")
	False
	"""
	scrambled = list(astring)
	checker = list(bstring)

	output = ""

	for letter in scrambled:
		if letter in checker:
			output += letter
			checker.remove(letter)
	return len(output) == len(bstring)

#####################################################################
if __name__ == "__main__":
	print
	import doctest
	if doctest.testmod().failed == 0:
		print "*** ALL TESTS PASSED ***"
