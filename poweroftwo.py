def power_of_two(num):
	"""take the num parameter being passed which will be an integer 
	and return the string true if it's a power of two. If it's not return the 
	string false. For example if the input is 16 then your program should return 
	the string true but if the input is 22 then the output should be the string false. 

	Example::
	>>> power_of_two(4)
	True
	>>> power_of_two(124)
	False

	"""
	if num % 2 != 0:
		return False

	power_num = 1

	while power_num < num:

		power_num *= 2

		if power_num == num:
			return True
			
	return False

#####################################################################
if __name__ == "__main__":
	print
	import doctest
	if doctest.testmod().failed == 0:
		print "*** ALL TESTS PASSED ***"
   