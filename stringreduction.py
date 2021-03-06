def string_reduction(string):
	"""have the function StringReduction(str) take the str parameter being passed and return the smallest 
	number you can get through the following reduction method. The method is: Only the letters a, b, and c will 
	be given in str and you must take two different adjacent characters and replace it with the third. For example 
	"ac" can be replaced with "b" but "aa" cannot be replaced with anything. This method is done repeatedly until the 
	string cannot be further reduced, and the length of the resulting string is to be outputted. For example: if str is 
	"cab", "ca" can be reduced to "b" and you get "bb" (you can also reduce it to "cc"). The reduction is done so the output 
	should be 2. If str is "bcab", "bc" reduces to "a", so you have "aab", then "ab" reduces to "c", and the final string "ac" 
	is reduced to "b" so the output should be 1. 
	Example::
	>>> string_reduction('abcabc')
	2
	>>> string_reduction('cccc')
	4
	"""
	string_replace = {
						'ac':'b', 
						'ca':'b',
						'ca':'cc',
						'bc':'a',
						'ab':'c',
						'ba':'c',
						'cb':'a'
					  }

	for letter in string:
		string = string.replace('ac','b')
		string = string.replace('ca','b')
		string = string.replace('bc','a')
		string = string.replace('ab','c')
		string = string.replace('ba','c')
		string = string.replace('cb','c')
	return len(string)

#####################################################################
if __name__ == "__main__":
	print
	import doctest
	if doctest.testmod().failed == 0:
		print "*** ALL TESTS PASSED ***"
     
