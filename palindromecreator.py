def is_palindrome(string):
	if string == string[::-1]:
		return True
	return False


def palindrome_creator(string):
	"""have the function PalindromeCreator(str) take the str parameter being 
	passed and determine if it is possible to create a palindromic string of 
	at least 3 characters by removing 1 or 2 characters. For example: if str 
	is "abcjchba" then you can remove the characters jh to produce "abccba" 
	which is a palindrome. For this example your program should return the two 
	characters that were removed with no delimiter and in the order they appear 
	in the string, so jh. If 1 or 2 characters cannot be removed to produce a 
	palindrome, then return the string not possible. If the input string is 
	already a palindrome, your program should return the string palindrome.
	Example::
	>>> palindrome_creator("mmop")
	'not possible'

	>>> palindrome_creator("kjjjhjjj") 
	'k'
	"""

	if is_palindrome(string):
		return 'palindrome'

	for i in range(0, len(string)):
		one_char = string[0:i] + string[i + 1:]
		if is_palindrome(one_char):
			return string[i] 
	for i in range(0, len(string) - 1):
		two_char = string[0:i] + string[i +2:]
		if is_palindrome(two_char) and len(two_char) > 2:
			return string[i: i + 1]
	return 'not possible'

#####################################################################
if __name__ == "__main__":
	print
	import doctest
	if doctest.testmod().failed == 0:
		print "*** ALL TESTS PASSED ***"
   