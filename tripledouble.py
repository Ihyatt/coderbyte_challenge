def triple_double(num1, num2):
	"""have the function TripleDouble(num1,num2) take both parameters being passed, 
	and return 1 if there is a straight triple of a number at any place in num1 and also 
	a straight double of the same number in num2. For example: if num1 equals 451999277 and 
	num2 equals 41177722899, then return 1 because in the first parameter you have the straight 
	triple 999 and you have a straight double, 99, of the same number in the second parameter. If 
	this isn't the case, return 0. 
	Example::
	>>> triple_double(465555, 5579)
	1

	>>> triple_double(67844, 66237)
	0
	"""
	if len(str(num1)) < 3:
		return 0
	elif len(str(num2)) < 2:
		return 0 

	count_num1 = []
	count_num2 = []

	count = 1
	current = str(num1)[0]
	for num in str(num1)[1:]:
		if current != num:
			if count > 2:
				count_num1.append(count)
			current = num
			count = 1
		else: 
			count += 1
	if count > 2:
		count_num1.append(count)



	count = 1
	current = str(num2)[0]
	for num in str(num2)[1:]:
		if current != num:
			if count > 1:
				count_num2.append(count)
			current = num
			count = 1
		else: 
			count += 1
	if count > 1: 
		count_num2.append(count)
	

	if len(count_num1) > 0 and len(count_num2) > 0:
		return 1
	else:
		return 0 

	

		

		
			

		
		
		


#####################################################################
if __name__ == "__main__":
	print
	import doctest
	if doctest.testmod().failed == 0:
		print "*** ALL TESTS PASSED ***"


