def word_count(string):
	"""take the str string parameter being passed and return the number of words the string contains
	(ie. "Never eat shredded wheat" would return 4). Words will be separated by single spaces.
	Example::
	>>> word_count("Hello World")
	2
	>>> word_count("one 22 three")
	3


	"""
	word_counter = string.split(" ")
	count = 0 
	for word in word_counter:
		count += 1

	return count


#####################################################################
if __name__ == "__main__":
	print
	import doctest
	if doctest.testmod().failed == 0:
		print "*** ALL TESTS PASSED ***"