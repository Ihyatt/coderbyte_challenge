def third_greatest(lst):
	""" take the array of strings stored in strArr and return the third largest 
	word within in. So for example: if strArr is ["hello", "world", "before", "all"] your
	output should be world because "before" is 6 letters long, and "hello" and "world" are both 
	5, but the output should be world because it appeared as the last 5 letter word in the array. 
	If strArr was ["hello", "world", "after", "all"] the output should be after because the first 
	three words are all 5 letters long, so return the last one. The array will have at least three 
	strings and each string will only contain letters. 

	Example::
	>>> third_greatest(["coder","byte","code"])
	'code'
	>>> third_greatest(["abc","defg","z","hijk"])
	'abc'

	"""
	first = None
	second = None
	third = None

	for word in lst:
		if first is None or len(word) > len(first):
			third = second
			second = first
			first = word
		elif second is None or len(word) > len(second):
			third = second
			second = word
		elif third is None or len(word) > len(third):
			third = word

	return third
	








#####################################################################
if __name__ == "__main__":
	print
	import doctest
	if doctest.testmod().failed == 0:
		print "*** ALL TESTS PASSED ***"
   