def ab_check(string):
	""" take the str parameter being passed and return the string true if 
	the characters a and b are separated by exactly 3 places anywhere in the
	string at least once
	Example::

	>>> ab_check("after badly")
	False
	>>> ab_check("Laura sobs")
	True

	"""
	ab_checker = list(string)
	idx = 0 
	while idx < len(ab_checker) - 4:
		if ab_checker[idx] == "a":
			if ab_checker[idx + 4] == "b":
				return True
		idx += 1
	return False


#####################################################################
if __name__ == "__main__":
	print
	import doctest
	if doctest.testmod().failed == 0:
		print "*** ALL TESTS PASSED ***"
   


