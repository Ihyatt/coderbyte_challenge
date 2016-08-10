def binary_reversal(string):
	"""Have the function BinaryReversal(str) take the str parameter being passed, 
	which will be a positive integer, take its binary representation, reverse that 
	string of bits, and then finally return the new reversed string in decimal form. 
	For example: if str is "47" then the binary version of this integer is 00101111. 
	Your program should reverse this binary string which then becomes: 11110100 and then 
	finally return the decimal version of this string, which is 244. 
	Example::

	>>> binary_reversal(47)
	"244"
	>>> binary_reversal("213")
	"171"
	>>> binary_reversal("4567")
	"60296"
	"""
	binary = bin(int(string))
	new_binary = binary.replace('b', '0')
	new_binary = new_binary[::-1]
	
	dec = int(new_binary, 2)
	print dec


#####################################################################
if __name__ == "__main__":
	print
	import doctest
	if doctest.testmod().failed == 0:
		print "*** ALL TESTS PASSED ***"
   