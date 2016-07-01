import math
def div_string(num1, num2):
	"""Take both parameters being passed, divide num1 by num2, and 
	return the result as a string with properly formatted commas. If an answer 
	is only 3 digits long, return the number with no commas (ie. 2 / 3 should output "1"). 
	For example: if num1 is 123456789 and num2 is 10000 the output should be "12,346 
	Example::
	>>> div_string(5, 2)
	'3'

	>>> div_string(6874, 67)
	'103'

	>>> div_string(123456789, 10000)
	'12,346'

	"""
	div_num = str(int(math.ceil(float(num1) / float(num2))))
	lst = []
	
	
	if len(div_num) > 3:

		rev_div_num = reversed(list(div_num))
		

		insert = 0 
		for num in rev_div_num:

			insert += 1
			
			if insert == 3:
				num = ',' + num
			
				lst.append(num)
				insert = 0 
			else: 
				lst.append(num)
		lst = lst[::-1]
		return ''.join(lst)
	return div_num





	



	

#####################################################################
if __name__ == "__main__":
	print
	import doctest
	if doctest.testmod().failed == 0:
		print "*** ALL TESTS PASSED ***"
     







