def offline_min(lst):
	"""Take the strArr parameter being passed which will be an array of 
	integers ranging from 1...n and the letter "E" and return the correct 
	subset based on the following rules. The input will be in the following 
	format: ["I","I","E","I",...,"E",...,"I"] where the I's stand for integers 
	and the E means take out the smallest integer currently in the whole set. 
	When finished, your program should return that new set with integers separated 
	by commas. For example: if strArr is ["5","4","6","E","1","7","E","E","3","2"] 
	then your program should return 4,1,5.

	Example::
	>>> offline_min(["1","2","E","E","3"])
	['1', '2']
	>>> offline_min(["4","E","1","E","2","E","3","E"])
	['4', '1', '2', '3']

	"""
	nums = []
	output = []
	e_count = lst.count('E')

	for num in lst:
		if num != 'E':
			nums.append(num)
		else:
			smallest = min(nums)
			nums.remove(smallest)
			output.append(smallest)

	return output

	



#####################################################################
if __name__ == "__main__":
	print
	import doctest
	if doctest.testmod().failed == 0:
		print "*** ALL TESTS PASSED ***"


