import itertools
def permutation_step(num):
	"""have the function PermutationStep(num) take the num parameter being passed and 
	return the next number greater than num using the same digits. For example: if num 
	is 123 return 132, if it's 12453 return 12534. If a number has no greater permutations, 
	return -1 (ie. 999). 
	Example::
	>>> permutation_step(11121)
	11211

	>>> permutation_step(41352)
	41523

	>>> permutation_step(321)
	-1
	"""
	perms = list(itertools.permutations(list(str(num))))
	nums = []
	greater = None
	for perm in perms: 
		perm = ''.join(list(perm))
		nums.append(int(perm))

	nums = sorted(nums)

	for n in nums:
		if n > num:
			greater = n
			break
	if greater == None:
		return -1 
	return greater
		
		


#####################################################################
if __name__ == "__main__":
	print
	import doctest
	if doctest.testmod().failed == 0:
		print "*** ALL TESTS PASSED ***"