def bracket_matcher(string):
	"""have the function BracketMatcher(str) take the str parameter being passed and return 
	1 if the brackets are correctly matched and each one is accounted for. Otherwise return 0. 
	For example: if str is "(hello (world))", then the output should be 1, but if str is "((hello 
	(world))" the the output should be 0 because the brackets do not correctly match up. Only "(" and ")" 
	will be used as brackets. If str contains no brackets return 1. 
	Example::
	>>> bracket_matcher( '(coder)(byte))0' )
	0
	>>> bracket_matcher( '(c(oder)) b(yte)' )
	1
	"""
	bracket_front = '('

	bracket_checker = ['(',')']

	brackets = []

	for bracket in string:
		if bracket in bracket_checker:
			brackets.append(bracket)
	count = 0 
	for bracket in brackets:
		if bracket == '(':
			count += 1
		elif bracket == ')':
			if count == 0:
				return 0
			count -= 1
	
	if count == 0:
		return 1
	return 0 
		




#####################################################################
if __name__ == "__main__":
	print
	import doctest
	if doctest.testmod().failed == 0:
		print "*** ALL TESTS PASSED ***"
