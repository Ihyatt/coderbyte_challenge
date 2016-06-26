def simple_adding(num):
	""" add up all the numbers from 1 to num.
	Example::
	>>> simple_adding(12)
	78

	>>> simple_adding(140)
	9870

	"""

	if num == 0:
		return 0 

	return num + simple_adding(num - 1)


#####################################################################
if __name__ == "__main__":
	print
	import doctest
	if doctest.testmod().failed == 0:
		print "*** ALL TESTS PASSED ***"
   

