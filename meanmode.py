def mean_mode(lst):
	""" take the array of numbers stored in arr and return 1 if the mode equals 
	the mean, 0 if they don't equal each other (ie. [5, 3, 3, 3, 1] should return 
	1 because the mode (3) equals the mean (3)). The array will not be empty, 
	will only contain positive integers, and will not contain more than one mode. 
	Example::
	>>> mean_mode([1, 2, 3])
	0
	>>> mean_mode([4, 4, 4, 6, 2])
	1
	"""""

	num_freq = {}
	greatest = 1
	mode = None

	mean = (sum(lst)) / len(lst)
	
	for num in lst:
		if num in num_freq:
			num_freq[num] += 1
		else: 
			num_freq[num] = 1

	for num in num_freq:
		if num_freq[num] > greatest:
			greatest = num_freq[num]
			mode = num

	if mode == mean:
		return 1
	else: 
		return 0 

	

	

#####################################################################
if __name__ == "__main__":
	print
	import doctest
	if doctest.testmod().failed == 0:
		print "*** ALL TESTS PASSED ***"
