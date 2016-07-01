import re
import numbers
def number_addition(string):

	"""take the str parameter, search for all the numbers in the string, 
	add them together, then return that final number. For example: if str is 
	"88Hello 3World!" the output should be 91. You will have to differentiate between 
	single digit numbers and multiple digit numbers like in the example above. So "55Hello" and 
	"5Hello 5" should return two different answers. Each string will contain at least one letter or 
	symbol. 
 
	Example::
	>>> number_addition("75Number9")
	84
	>>> number_addition("10 2One Number*1*")
	13
	"""
	nums = []
	nums_letters = re.split('(\d+)', string)
	for num in nums_letters:
		if num.isdigit():
			nums.append(int(num))
	return sum(nums)
    		
 




#####################################################################
if __name__ == "__main__":
	print
	import doctest
	if doctest.testmod().failed == 0:
		print "*** ALL TESTS PASSED ***"
   



