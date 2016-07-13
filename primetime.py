def prime_time(num):
	"""Have the function PrimeTime(num) take the num parameter being passed and 
	return the string true if the parameter is a prime number, otherwise return 
	the string false. The range will be between 1 and 2^16. 
	Example::
	>>> prime_time(19)
	True

	>>> prime_time(110)
	False
	"""

	for n in range(2, num):
		if num % n == 0:
			return False
	return True

#####################################################################
if __name__ == "__main__":
	print
	import doctest
	if doctest.testmod().failed == 0:
		print "*** ALL TESTS PASSED ***"