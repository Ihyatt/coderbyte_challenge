from itertools import permutations

def largest_pair(num):
	""" have the function LargestPair(num) take the num parameter being passed and determine 
	the largest double digit number within the whole number. For example: if num is 4759472 
	then your program should return 94 because that is the largest double digit number. The 
	input will always contain at least two positive digits. 
	Example::
	>>> largest_pair(453857)
	85
	>>> largest_pair(363223311)
	63
	"""
	largest = 1

	nums = str(num)

	idx = 0 
	while idx < len(nums) - 1:
		double_dig =  int(nums[idx] + nums[idx + 1])
		if double_dig > largest:
			largest = double_dig

		idx += 1
	return largest



	
#####################################################################
if __name__ == "__main__":
	print
	import doctest
	if doctest.testmod().failed == 0:
		print "*** ALL TESTS PASSED ***"
   
