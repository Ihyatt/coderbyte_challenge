def three_five_multiples(num):
	"""have the function ThreeFiveMultiples(num) return the sum of all the multiples of 3 and 5 that are below num. 
	For example: if num is 10, the multiples of 3 and 5 that are below 10 are 3, 5, 6, and 9, and adding them up you 
	get 23, so your program should return 23. The integer being passed will be between 1 and 100. 
	Example::
	>>> three_five_multiples(6)
	8
	>>> three_five_multiples(1)
	0
	"""

	three_five_mult = []

	for i in range(1,num):
		if i % 5 == 0:
			three_five_mult.append(i)
		elif i % 3 == 0:
			three_five_mult.append(i)

	if three_five_mult == []:
		return 0 
	else:
		return sum(three_five_mult)


#####################################################################
if __name__ == "__main__":
	print
	import doctest
	if doctest.testmod().failed == 0:
		print "*** ALL TESTS PASSED ***"
     
