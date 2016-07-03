def bitwise_one(lst):
	"""Have the function BitwiseOne(strArr) take the array of strings stored in strArr, 
	which will only contain two strings of equal length that represent binary numbers, 
	and return a final binary string that performed the bitwise OR operation on both strings. 
	A bitwise OR operation places a 0 in the new string where there are zeroes in both binary strings, 
	otherwise it places a 1 in that spot. For example: if strArr is ['1001', '0100'] then your program 
	should return the string '1101' 
	Example::
	>>> bitwise_one(['100', '000'])
	'100'
	>>> bitwise_one(['00011', '01010'])
	'01011'

	"""

	bit_output = ""

	bit_one = list(lst[0])
	bit_two = list(lst[1])

	while len(bit_one) > 0:
		if bit_one[0] == '1':
			bit_output += bit_one[0]
		elif bit_two[0] == '1':
			bit_output += bit_two[0]
		else:
			bit_output += '0'
		bit_one.pop(0)
		bit_two.pop(0)

	return bit_output


#####################################################################
if __name__ == "__main__":
	print
	import doctest
	if doctest.testmod().failed == 0:
		print "*** ALL TESTS PASSED ***"
     
