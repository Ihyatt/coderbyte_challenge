def dash_insertii(num):
	"""have the function DashInsertII(str) insert dashes ('-') between each two odd numbers and insert asterisks ('*') 
	between each two even numbers in str. For example: if str is 4546793 the output should be 454*67-9-3.
	Don't count zero as an odd or even number. 
	Example::
	>>> dash_insertii(99946)
	'9-9-94*6'

	>>> dash_insertii(56647304)
	'56*6*47-304'
	"""

	astr_dash = ''

	str_nums = list(str(num))

	str_num = ''

	idx = 0 
	while idx < len(str_nums) - 1:
		if str_nums[idx] != '0':

			if int(str_nums[idx]) % 2 == 0 and int(str_nums[idx + 1]) % 2 == 0:
				str_num += str_nums[idx] + '*'
			elif int(str_nums[idx]) % 2 != 0 and int(str_nums[idx + 1]) % 2 != 0:
				str_num += str_nums[idx] + '-' 
			else: 
				str_num += str_nums[idx]
		else:
			str_num += str_nums[idx]
		idx += 1

	str_num = str_num + str_nums[-1]
	return str_num

#####################################################################
if __name__ == "__main__":
	print
	import doctest
	if doctest.testmod().failed == 0:
		print "*** ALL TESTS PASSED ***"



