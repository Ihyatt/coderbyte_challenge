def additive_pers(num):
	""" take the num parameter being passed which will always be a 
	positive integer and return its additive persistence which is the 
	number of times you must add the digits in num until you reach a 
	single digit. For example: if num is 2718 then your program should 
	return 2 because 2 + 7 + 1 + 8 = 18 and 1 + 8 = 9 and you stop at 9. 

	Example::
	>>> additive_pers(4)
	0 
	>>> additive_pers(19)
	2
	"""

	count = 0 
	if len(str(num)) == 1:
		return count

	str_num = str(num)

	while True: 

		nums = list(str_num)
		
		sums = 0 
		for num in nums:
			sums += int(num)
		
		count += 1
		if len(str(sums)) == 1:
			break
		
		str_num = str(sums)
		
	return count
		



#####################################################################
if __name__ == "__main__":
	print
	import doctest
	if doctest.testmod().failed == 0:
		print "*** ALL TESTS PASSED ***"
   



