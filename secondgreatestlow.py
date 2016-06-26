def second_greatest_low(lst):
	""" Take the array of numbers stored in arr and return the 
	second lowest and second greatest numbers, respectively, separated by a space. 
	For example: if arr contains [7, 7, 12, 98, 106] the output should be 12 98. 
	The array will not be empty and will contain at least 2 numbers. It can get tricky if there's just two numbers!

	Example::
	>>> second_greatest_low([42, 1, 42, 180])
	'42 42'
	>>> second_greatest_low([4, 90])
	'90 4'
	"""
	second_lowest = None
	second_greatest = None
	sorted_nums = sorted(lst)

	second_lowest = sorted_nums[1]
	second_greatest = sorted_nums[-2]

	return str(second_lowest) + " " + str(second_greatest)

#####################################################################
if __name__ == "__main__":
	print
	import doctest
	if doctest.testmod().failed == 0:
		print "*** ALL TESTS PASSED ***"
     


