def binary_converter(string):
	"""have the function BinaryConverter(str) return the decimal form of 
	the binary value. For example: if 101 is passed return 5, or if 1000 
	is passed return 8. 
	Example::
	>>> binary_converter('100101')
	'37'

	>>> binary_converter('011')
	'3'
	"""

	output = 0 
	multi = 1

	for num in string[::-1]:
		output += int(num) * multi
		multi *= 2
		
	return str(output)


#####################################################################
if __name__ == "__main__":
	print
	import doctest
	if doctest.testmod().failed == 0:
		print "*** ALL TESTS PASSED ***"
