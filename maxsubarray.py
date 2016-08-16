def max_subarray(lst):
	"""Using the Python language, have the function MaxSubarray(arr) take the array of numbers 
	stored in arr and determine the largest sum that can be formed by any contiguous subarray in 
	he array. For example, if arr is [-2, 5, -1, 7, -3] then your program should return 11 because 
	the sum is formed by the subarray [5, -1, 7]. Adding any element before or after this subarray 
	would make the sum smaller.

	Example::

	>>> max_subarray([1, -2, 0, 3])
	3
	>>> max_subarray([3, -1, -1, 4, 3, -1])
	8

	"""
	slices = []
	greatest = lst[0]

	for i in range(0, len(lst)):
		for j in range(i, len(lst) + 1):
			slices.append(lst[i:j])


	for sub in slices:
		sums = sum(sub)
		if sums > greatest:
			greatest = sums
	return greatest






#####################################################################
if __name__ == "__main__":
	print
	import doctest
	if doctest.testmod().failed == 0:
		print "*** ALL TESTS PASSED ***"
   

