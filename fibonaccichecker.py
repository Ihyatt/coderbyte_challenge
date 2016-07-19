def fibonacci(num):
	"""have the function FibonacciChecker(num) return the string yes if the number given is part 
	of the Fibonacci sequence. This sequence is defined by: Fn = Fn-1 + Fn-2, which means to find 
	Fn you add the previous two numbers up. The first two numbers are 0 and 1, then comes 1, 2, 3, 5 
	etc. If num is not in the Fibonacci sequence, return the string no. 
	Example:: 
	>>> fibonacci(34)
	'yes'

	>>> fibonacci(54)
	'no'
	"""

	a,b = 1,1
	while b < num:
		a,b = b, a + b
	if b == num:
		return 'yes'
	return 'no'

#####################################################################
if __name__ == "__main__":
	print
	import doctest
	if doctest.testmod().failed == 0:
		print "*** ALL TESTS PASSED ***"
     