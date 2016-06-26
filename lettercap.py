def letter_capitalize(str):
	""" Take the str parameter being passed and capitalize the first 
	letter of each word. Words will be separated by only one space.
	Example::
	>>> letter_capitalize('hello world') 
	'Hello World'
	>>> letter_capitalize('i ran there')
	'I Ran There'

	"""
	new_str = []
	str = str.split(" ")
	for word in str:
		new_word =  word[0].upper() + word[1:] 
		new_str.append(new_word)
	return " ".join(new_str)



#####################################################################
if __name__ == "__main__":
	print
	import doctest
	if doctest.testmod().failed == 0:
		print "*** ALL TESTS PASSED ***"
   
