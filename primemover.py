def prime_checker(num):

	if num < 2: 
		return False
	for n in range(2,num):
		if num % n == 0: 
			return False
	return True


def prime_mover(num):
	"""have the function PrimeMover(num) return the numth prime number. 
	The range will be from 1 to 10^4. For example: if num is 16 the output 
	should be 53 as 53 is the 16th prime number. 
	Example::
	>>> prime_mover(9)
	23
	>>> prime_mover(100)
	541
	"""

	primes = []

	number = 0 
	while len(primes) < num:
		if prime_checker(number):
			primes.append(number)
		number += 1
	return primes[-1]

#####################################################################
if __name__ == "__main__":
	print
	import doctest
	if doctest.testmod().failed == 0:
		print "*** ALL TESTS PASSED ***"

