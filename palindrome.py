def palindrome_check(string):
	"""take the str parameter being passed and return the string true if the parameter 
	is a palindrome, (the string is the same forward as it is backward) otherwise return the string false. 
	For example: "racecar" is also "racecar" backwards. Punctuation and numbers will not be part of the string. 
	Example::
	>>> palindrome_check("never odd or even")
	True
	>>> palindrome_check("eye")
	True
	"""

	
	string = string.replace(" ", "")
	return string[::1] == string[::-1]

#####################################################################
if __name__ == "__main__":
	print
	import doctest
	if doctest.testmod().failed == 0:
		print "*** ALL TESTS PASSED ***"
     