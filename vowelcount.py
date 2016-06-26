def vowel_count(string):
	"""take the str string parameter being passed and return 
	the number of vowels the string contains (ie. "All cows eat grass" would return 5).
	Example::
	>>> vowel_count("hello")
	2
	>>> vowel_count("coderbyte")
	3
	"""
	vowels = ["a", "e", "i","o", "u"]
	count = 0 
	for i in range(0, len(string)):
		if string[i] in vowels: 
			count += 1
	return count


#####################################################################
if __name__ == "__main__":
	print
	import doctest
	if doctest.testmod().failed == 0:
		print "*** ALL TESTS PASSED ***"