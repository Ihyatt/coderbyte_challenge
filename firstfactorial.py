def first_factorial(num):

	"""Take the num parameter being passed and return the factorial of it
	Example::
	>>> first_factorial(4)
	24

	>>> first_factorial(8)
	40320 """

	factorial = 1
	for i in range(1,num + 1):
		factorial *= i 

	return factorial




#####################################################################
if __name__ == "__main__":
	print
	import doctest
	if doctest.testmod().failed == 0:
		print "*** ALL TESTS PASSED ***"
   