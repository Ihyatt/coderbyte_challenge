def changing_seq(lst):
	"""Take the array of numbers stored in arr and return the index 
	at which the numbers stop increasing and begin decreasing or stop 
	decreasing and begin increasing. For example: if arr is [1, 2, 4, 6, 4, 3, 1] 
	then your program should return 3 because 6 is the last point in the array where
	the numbers were increasing and the next number begins a decreasing sequence. 
	The array will contain at least 3 numbers and it may contains only a single sequence,
	increasing or decreasing. If there is only a single sequence in the array, then your 
	program should return -1. Indexing should begin with 0.

	Example::
	>>> changing_seq([-4, -2, 9, 10])
	-1
	>>> changing_seq([5, 4, 3, 2, 10, 11])
	3
	"""
	seq_idx = -1
	if lst[0] > lst[1]:
		idx = 0 
		while idx < len(lst) - 1:
			if lst[idx] < lst[idx + 1]:
				seq_idx = idx
				break
			idx += 1

	elif lst[0] < lst[1]:
		idx = 0 
		while idx < len(lst) - 1:
			if lst[idx] > lst[idx + 1]:
				seq_idx = idx
				break
			idx += 1
	return seq_idx



#####################################################################
if __name__ == "__main__":
	print
	import doctest
	if doctest.testmod().failed == 0:
		print "*** ALL TESTS PASSED ***"
     

