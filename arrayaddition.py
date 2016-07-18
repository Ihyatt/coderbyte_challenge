import itertools
def array_addition(lst):
	"""Using the Python language, have the function ArrayAddition(arr) 
	take the array of numbers stored in arr and return the string true if any 
	combination of numbers in the array can be added up to equal the largest number
	in the array, otherwise return the string false. For example: if arr contains [4, 6, 23, 10, 1, 3] 
	the output should return true because 4 + 6 + 10 + 3 = 23. The array will not be empty, will not contain 
	all the same elements, and may contain negative numbers. 
	>>> array_addition([5,7,16,1,2])
	True
	>>> array_addition([3,5,-1,8,12])
	True
	"""

	perms = []
	max_num = max(lst)
	lst = sorted(lst)

	idx = 1 
	while idx < len(lst) - 1:
		perms.append(list(itertools.permutations(lst, idx)))
		idx += 1
	
	for lists in perms:
		for nums in lists:
			if sum(nums) == max_num:
				return True

	return False




#####################################################################
if __name__ == "__main__":
	print
	import doctest
	if doctest.testmod().failed == 0:
		print "*** ALL TESTS PASSED ***"


