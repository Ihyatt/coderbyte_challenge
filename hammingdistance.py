def hamming_dist(lst):
	"""Have the function HammingDistance(strArr) take the array of strings stored in 
	strArr, which will only contain two strings of equal length and return the Hamming 
	distance between them. The Hamming distance is the number of positions where the corresponding 
	characters are different. For example: if strArr is ["coder", "codec"] then your program should 
	return 1. The string will always be of equal length and will only contain lowercase characters from 
	the alphabet and numbers. 
	Example::
	>>> hamming_dist(["10011", "10100"])
	3
	>>> hamming_dist(["helloworld", "worldhello"])
	8
	"""
	count = 0 

	output = ""

	checker_one = list(lst[0])
	checker_two = list(lst[1])

	while len(checker_one) > 0: 
		if checker_one[0] != checker_two[0]:
			count += 1
		checker_one.pop(0)
		checker_two.pop(0)

	return count


#####################################################################
if __name__ == "__main__":
	print
	import doctest
	if doctest.testmod().failed == 0:
		print "*** ALL TESTS PASSED ***"
     

