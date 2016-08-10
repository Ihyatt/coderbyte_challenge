def pali_checker(num):
	str_num = str(num)
	if str_num == str_num[::-1]:
		return True
	return False

def next_palindrome(num):
	"""have the function NextPalindrome(num) take the num parameter being passed and 
	return the next largest palindromic number. The input can be any positive integer. 
	For example: if num is 24, then your program should return 33 because that is the next 
	largest number that is a palindrome. 
	Example::
	>>> next_palindrome(2)
	3
	>>> next_palindrome(180)
	181
	"""
	if num < 9:
		return num + 1
	greater = num
	while True:
		greater += 1
		if pali_checker(greater):
			break
	return greater



#####################################################################
if __name__ == "__main__":
	print
	import doctest
	if doctest.testmod().failed == 0:
		print "*** ALL TESTS PASSED ***"
   