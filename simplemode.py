def simple_mode(lst):
	"""have the function SimpleMode(arr) take the array of numbers 
	stored in arr and return the number that appears most frequently 
	(the mode). For example: if arr contains [10, 4, 5, 2, 4] the output 
	should be 4. If there is more than one mode return the one that appeared 
	in the array first (ie. [5, 10, 10, 6, 5] should return 5 because it appeared 
	first). If there is no mode return -1. The array will not be empty. 
	Example::
	>>> simple_mode([5,5,2,2,1])
	5
	>>> simple_mode([3,4,1,6,10])
	-1
	"""
	
	mode = None
	freq = 1

	for num in lst: 
		if lst.count(num) > freq:
			mode = num
			freq = lst.count(num)

	if mode == None:
		return - 1
	else:
		return mode

#####################################################################
if __name__ == "__main__":
	print
	import doctest
	if doctest.testmod().failed == 0:
		print "*** ALL TESTS PASSED ***"
