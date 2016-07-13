def palindrome_two(astring):
	"""have the function PalindromeTwo(str) take the str parameter 
	being passed and return the string true if the parameter is a palindrome, 
	(the string is the same forward as it is backward) otherwise return the string 
	false. The parameter entered may have punctuation and symbols but they should 
	not affect whether the string is in fact a palindrome. For example: "Anne, I 
	vote more cars race Rome-to-Vienna" should return true. 
	Example::
	>>> palindrome_two("Noel - sees Leon")
	True
	>>> palindrome_two("A war at Tarawa!")
	True
	"""
	pali_checker = ""

	for letter in astring:
		if letter.isalpha():
			pali_checker += letter

	if pali_checker.lower() == pali_checker.lower()[::-1]:
		return True
	return False

#####################################################################
if __name__ == "__main__":
	print
	import doctest
	if doctest.testmod().failed == 0:
		print "*** ALL TESTS PASSED ***"
   
