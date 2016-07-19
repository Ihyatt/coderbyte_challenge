def multibrackets(string):
	"""have the function MultipleBrackets(str) take the str parameter being passed and return 1 #ofBrackets if 
	the brackets are correctly matched and each one is accounted for. Otherwise return 0. For example: if str is 
	"(hello [world])(!)", then the output should be 1 3 because all the brackets are matched and there are 3 pairs 
	of brackets, but if str is "((hello [world])" the the output should be 0 because the brackets do not correctly 
	match up. Only "(", ")", "[", and "]" will be used as brackets. If str contains no brackets return 1. 
	Example::
	>>> multibrackets("(coder)[byte)]")
	0
	>>> multibrackets("(c([od]er)) b(yt[e])")
	'1 5'

	"""

	curve_count = 0 
	square_count = 0 
	bracket_count = 0 

	for bracket in string:
		if bracket == "(":
			curve_count += 1
		elif bracket == ")":
			if curve_count == 0:
				return 0
			curve_count -= 1
			bracket_count += 1
		elif bracket == "[":
			square_count += 1
		elif bracket == "]":
			if square_count == 0:
				return 0
			square_count -= 1
			bracket_count += 1
	if square_count != 0 or curve_count != 0:
		return 0 
	else: 
		output = str(1) + " " + str(bracket_count)
		return output


#####################################################################
if __name__ == "__main__":
	print
	import doctest
	if doctest.testmod().failed == 0:
		print "*** ALL TESTS PASSED ***"
     

