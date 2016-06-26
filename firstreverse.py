def first_reverse(str):

	"""Have the function FirstReverse(str) take the str parameter being passed and return the string in reversed order.
	Example::

		>>> first_reverse('coderbyte')
		'etybredoc'

		>>> first_reverse('I Love Code')
		'edoC evoL I' """

	rev = str[::-1]
	return rev

	




#####################################################################
if __name__ == "__main__":
	print
	import doctest
	if doctest.testmod().failed == 0:
		print "*** ALL TESTS PASSED ***"
   