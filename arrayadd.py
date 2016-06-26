import itertools
def array_addition(lst):
	"""take the array of numbers stored in arr and return the string true if any 
	combination of numbers in the array can be added up to equal the largest number 
	in the array, otherwise return the string false. For example: if arr contains 
	[4, 6, 23, 10, 1, 3] the output should return true because 4 + 6 + 10 + 3 = 23. 
	The array will not be empty, will not contain all the same elements, and may contain 
	negative numbers. 
	Example::
	>>> array_addition([5,7,16,1,2])
	False
	>>> array_addition([3,5,-1,8,12])
	True
	"""


	greatest = max(lst)
	sorted_nums = sorted(lst)
	
	without_greatest = sorted_nums[:-1]

	total_sums = []
	
	
	idx = 1 
	while idx < len(without_greatest):
		perms = list(itertools.permutations(without_greatest, idx))
		for perm in perms:
			if sum(perm) == greatest:
				return True

		idx += 1
	return False
	


	


	

	

#####################################################################
if __name__ == "__main__":
	print
	import doctest
	if doctest.testmod().failed == 0:
		print "*** ALL TESTS PASSED ***"
     

