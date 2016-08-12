from itertools import permutations

def longest_seq(lst):
	""" have the function LongestIncreasingSequence(arr) take the array of positive 
	integers stored in arr and return the length of the longest increasing subsequence 
	(LIS). A LIS is a subset of the original list where the numbers are in sorted order, 
	from lowest to highest, and are in increasing order. The sequence does not need to be 
	contiguous or unique, and there can be several different subsequences. For example: if 
	arr is [4, 3, 5, 1, 6] then a possible LIS 
	is [3, 5, 6], and another is [1, 6]. For this input, your program should return 3 because 
	that is the length of the longest increasing subsequence. 
	Example::
	>>> longest_seq([9, 9, 4, 2])
	1
	
	"""
	uniq = list(set(lst))
	combo = []
	samples = []
	new_samples = []


	if sorted(lst) == lst and len(uniq) == len(lst):
		return len(lst)

	for i in reversed(range(2, len(lst) - 1)):
		combo.append(i)
	
	for test in combo:
		sample = list(permutations(lst, test))
		
		samples.append(sample)
	

	for sample in samples:
		new_sample = list(sample)
		new_samples.append(new_sample)

	for sublst in new_samples:
		if sublst == sublst.sort():
			return len(sublst)
	return 1








#####################################################################
if __name__ == "__main__":
	print
	import doctest
	if doctest.testmod().failed == 0:
		print "*** ALL TESTS PASSED ***"
   