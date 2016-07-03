def super_increasing(lst):
	"""Have the function Superincreasing(arr) take the array of numbers stored 
	in arr and determine if the array forms a superincreasing sequence where each 
	element in the array is greater than the sum of all previous elements. The array 
	will only consist of positive integers. For example: if arr is [1, 3, 6, 13, 54] 
	then your program should return the string 'true' because it forms a superincreasing 
	sequence. If a superincreasing sequence isn't formed, then your program should return 
	the string 'false' 
	Example::
	>>> super_increasing([1,2,3,4])
	False
	>>> super_increasing([1,2,5,10])
	True
	"""

	checker = None
	sums = 0 
	idx = 0

	while idx < len(lst) - 1:
		sums += lst[idx]
	
		if sums > lst[idx + 1]:
			return False
		idx += 1

	return True


#####################################################################
if __name__ == "__main__":
	print
	import doctest
	if doctest.testmod().failed == 0:
		print "*** ALL TESTS PASSED ***"
     
