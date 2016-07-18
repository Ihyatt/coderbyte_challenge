def arithgeoII(lst):
	"""Have the function ArithGeoII(arr) take the array of 
	numbers stored in arr and return the string "Arithmetic" 
	if the sequence follows an arithmetic pattern or return "Geometric" 
	if it follows a geometric pattern. If the sequence doesn't follow 
	either pattern return -1. An arithmetic sequence is one where the 
	difference between each of the numbers is consistent, where as in a 
	geometric sequence, each term after the first is multiplied by some constant
	or common ratio. Arithmetic example: [2, 4, 6, 8] and Geometric example: [2, 6, 18, 54]. 
	Negative numbers may be entered as parameters, 0 will not be entered, and no array will 
	contain all the same elements. 
	Example::
	>>> arithgeoII([5,10,15])
	'Arithmetic'
	>>> arithgeoII([2,4,16,24])
	-1
	>>> arithgeoII([2, 6, 18, 54])
	'Geometric'
	"""
	flag = -1
	arith = lst[1] - lst[0]
	geo = lst[1] / lst[0]

	idx = 0
	while idx < len(lst) - 1:
		if lst[idx + 1] - arith == lst[idx]:
			flag = 'Arithmetic'
		elif lst[idx + 1] / geo == lst[idx]:
			flag = 'Geometric'
		else: 
			flag = -1
		idx += 1

	return flag

#####################################################################
if __name__ == "__main__":
	print
	import doctest
	if doctest.testmod().failed == 0:
		print "*** ALL TESTS PASSED ***"

