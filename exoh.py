def ex_oh(str):
	"""take the str parameter being passed and return the string 
	true if there is an equal number of x's and o's, otherwise return the 
	string false. Only these two letters will be entered in the string, no punctuation or numbers.
	Example::

	>>> ex_oh("xooxxo")
	True
	>>> ex_oh("x")
	False

	"""
	xo_count = list(str)
	exes = xo_count.count("x")
	ohs = xo_count.count("o")
 	
 	return exes == ohs


#####################################################################
if __name__ == "__main__":
	print
	import doctest
	if doctest.testmod().failed == 0:
		print "*** ALL TESTS PASSED ***"