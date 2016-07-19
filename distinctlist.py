def distinct_list(lst):
	""" have the function DistinctList(arr) take the array of numbers stored in arr and 
	determine the total number of duplicate entries. For example if the input is [1, 2, 2, 2, 3] 
	then your program should output 2 because there are two duplicates of one of the elements. 
	Example::
	>>> distinct_list([0,-2,-2,5,5,5])
	3

	>>> distinct_list([100,2,101,4])
	0
	"""

	dup_check = {}


	for num in lst:
		if num in dup_check:
			dup_check[num] += 1
		else:
			dup_check[num] = 0 

	duplicates = 0 
	for num in dup_check:
		duplicates += dup_check[num]

	return duplicates



#####################################################################
if __name__ == "__main__":
	print
	import doctest
	if doctest.testmod().failed == 0:
		print "*** ALL TESTS PASSED ***"
     