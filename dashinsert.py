def dash_insert(num):
	"""Insert dashes ('-') between each two odd numbers in str. 
	For example: if str is 454793 the output should be 4547-9-3. 
	Don't count zero as an odd number. 

	Example::
	>>> dash_insert(99946)
	9-9-946

	>>> dash_insert(56730)
	567-30

	"""
	num_str = str(num)
	dash_str = ""

	idx = 0 
	while idx < len(num_str):
		if (int(num_str[idx]) % 2 != 0) and (int(num_str[idx + 1]) % 2 != 0):
			dash_str += num_str[idx] + "-"
		else: 
			dash_str += num_str[idx]
		idx += 1

	print dash_str


#####################################################################
if __name__ == "__main__":
	print
	import doctest
	if doctest.testmod().failed == 0:
		print "*** ALL TESTS PASSED ***"



