import itertools

def is_prime(num):
	if num < 2:
		return False

	for i in range(2,num):
		if num % i == 0:
			return False
	return True

def prime_checker(num):
	"""have the function PrimeChecker(num) take num and return 
	1 if any arrangement of num comes out to be a prime number, 
	otherwise return 0. For example: if num is 910, the output should 
	be 1 because 910 can be arranged into 109 or 019, both of which are primes. 
	Example::
	>>> prime_checker(98)
	1
	>>> prime_checker(598)
	1
	>>> prime_checker(221)
	0
	"""

	perms = list(itertools.permutations(list(str(num))))

	nums = []
	
	for perm in perms: 
		perm = ''.join(list(perm))
		nums.append(int(perm))

	for num in nums: 
		if is_prime(num):
			return 1
	return 0 




#####################################################################
if __name__ == "__main__":
	print
	import doctest
	if doctest.testmod().failed == 0:
		print "*** ALL TESTS PASSED ***"