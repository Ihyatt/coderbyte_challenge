def two_sum(lst):
	"""have the function TwoSum(arr) take the array of integers stored in arr, 
	and determine if any two numbers (excluding the first element) in the array 
	can sum up to the first element in the array. 
	Example::

	>>> two_sum([17, 4, 5, 6, 10, 11, 4, -3, -5, 3, 15, 2, 7])
	'6,11 10,7 15,2'

	>>> two_sum([7, 6, 4, 1, 7, -2, 3, 12])
	'6,1 4,3'
	"""

	first = lst[0]
	sums = []

	for i in range(1, len(lst)):
		for j in range(i, len(lst)):
			summed = lst[i] + lst[j]
			
			if summed == first:
			
				sums.append(str(lst[i]) + "," + str(lst[j]))
				
			summed = 0 

	return ' '.join(sums)


#####################################################################
if __name__ == "__main__":
	print
	import doctest
	if doctest.testmod().failed == 0:
		print "*** ALL TESTS PASSED ***"
   
