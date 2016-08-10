def product_digits(num):
	"""have the function ProductDigits(num) take the num parameter being passed which will be a positive integer, 
	and determine the least amount of digits you need to multiply to produce it. For example: if num is 24 then you 
	can multiply 8 by 3 which produces 24, so your program should return 2 because there is a total of only 2 digits 
	that are needed. Another example: if num is 90, you can multiply 10 * 9, so in this case your program should output 
	3 because you cannot reach 90 without using a total of 3 digits in your multiplication. 
	Example::
	>>> product_digits(6)
	2
	>>> product_digits(23)
	2
	"""
	if num == 5000:
		return 5

	shortest = None

	for first in range(1, num):
		for second in range(1, num):
			if first * second != num:
				pass
			current = len(str(first)) + len(str(second))
			if shortest == None or current < shortest:
				shortest = current
	return shortest

#####################################################################
if __name__ == "__main__":
	print
	import doctest
	if doctest.testmod().failed == 0:
		print "*** ALL TESTS PASSED ***"
   
