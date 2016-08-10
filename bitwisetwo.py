def bitwise_two(lst):
	"""have the function BitwiseTwo(strArr) take the array of strings stored 
	in strArr, which will only contain two strings of equal length that represent 
	binary numbers, and return a final binary string that performed the bitwise 
	AND operation on both strings. A bitwise AND operation places a 1 in the new 
	string where there is a 1 in both locations in the binary strings, otherwise 
	it places a 0 in that spot. For example: if strArr is ["10111", "01101"] then 
	your program should return the string "00101
	Example::
	>>> bitwise_two(["100", "000"])
	'000'

	>>> bitwise_two(["10100", "11100"])
	'10100'

	"""

	bit1 = list(lst[0])
	bit2 = list(lst[1])

	bit3 = ""

	while len(bit1) > 0:
		first1 = bit1[0]
		first2 = bit2[0]
		if first1 == "0" or first2 == "0":
			bit3 += "0"
		else:
			bit3 += "1"
		bit1.pop(0)
		bit2.pop(0)
	return bit3



#####################################################################
if __name__ == "__main__":
	print
	import doctest
	if doctest.testmod().failed == 0:
		print "*** ALL TESTS PASSED ***"
   
