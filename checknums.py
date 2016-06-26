def check_nums(num1, num2):
	""" take both parameters being passed and return the string
	true if num2 is greater than num1, otherwise return the string false
	Example::
	>>> check_nums(3, 122)
	True

	>>> check_nums(67, 67)
	'-1'

	"""

	if num1 < num2:
		return True
	else: 
		return '-1'

#####################################################################
if __name__ == "__main__":
	print
	import doctest
	if doctest.testmod().failed == 0:
		print "*** ALL TESTS PASSED ***"
   