def greatest_common_factor(num1,num2):
	"""have the function Division(num1,num2) take both parameters being 
	passed and return the Greatest Common Factor. That is, return the greatest
	number that evenly goes into both numbers with no remainder. For example:
	12 and 16 both are divisible by 1, 2, and 4 so the output should be 4. The 
	range for both parameters will be from 1 to 10^3. 
	Example::
	>>> greatest_common_factor(7,3)
	1
	>>> greatest_common_factor(36,54)
	18
	"""
	if num1 == num2:
		return num1
	greatest_factor = 1

	num1_factors = []
	num2_factors = []

	for n in range(1, num1 + 1):
		if num1 % n == 0: 
			num1_factors.append(n)

	for n in range(1, num2 + 1):
		if num2 % n == 0:
			num2_factors.append(n)



	if num1 > num2:
		for num in reversed(num2_factors):
			if num in num1_factors:
				greatest_factor = num
				return greatest_factor
	elif num1 < num2:
		for num in reversed(num1_factors):
			if num in num2_factors:
				greatest_factor = num
				return greatest_factor
				
	return greatest_factor

#####################################################################
if __name__ == "__main__":
	print
	import doctest
	if doctest.testmod().failed == 0:
		print "*** ALL TESTS PASSED ***"


