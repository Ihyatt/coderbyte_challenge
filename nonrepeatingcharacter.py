def non_repeating():
	"""have the function NonrepeatingCharacter(str) take the str parameter 
	being passed, which will contain only alphabetic characters and spaces, 
	and return the first non-repeating character. For example: if str is 
	"agettkgaeee" then your program should return k. The string will always 
	contain at least one character and there will always be at least one 
	non-repeating character. 
	Example::
	>>> non-repeating("abcdef")
	"a"

	>>> non-repeating("hello world hi hey")
	"w"
	"""


#####################################################################
if __name__ == "__main__":
	print
	import doctest
	if doctest.testmod().failed == 0:
		print "*** ALL TESTS PASSED ***"
   
