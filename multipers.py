def multi_pers(num):
	"""take the num parameter being passed which will always be a positive integer and 
	return its multiplicative persistence which is the number of times you must multiply the 
	digits in num until you reach a single digit. For example: if num is 39 then your program should 
	return 3 because 3 * 9 = 27 then 2 * 7 = 14 and finally 1 * 4 = 4 and you stop at 4. 

	Example::

	>>> multi_pers(4)
	0 
	>>> multi_pers(25)
	2

	"""

	count = 0 
	if len(str(num)) == 1:
		return count

	str_num = str(num)

	while True: 

		nums = list(str_num)
		
		multi = 1 
		for num in nums:
			multi *= int(num)
		
		count += 1
		if len(str(multi)) == 1:
			break
		
		str_num = str(multi)
		
	return count
		
#####################################################################
if __name__ == "__main__":
	print
	import doctest
	if doctest.testmod().failed == 0:
		print "*** ALL TESTS PASSED ***"
   