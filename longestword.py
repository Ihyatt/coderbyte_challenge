def longest_word(sen): 
	""""take the sen parameter being passed and return the largest word in the string. 
	If there are two or more words that are the same length, 
	return the first word from the string with that length. Ignore punctuation and assume sen will not be empty. 
	Example::
	>>> longest_word('fun&!! time')
	'time'

	>>> longest_word('I love dogs')
	'love'

	"""
	
	sen = sen.translate(None, "~!@#$%^&*()-_+={}[]:;'<>?/,.|`")

	largest = "a"
	new_sen = sen.split(" ")
	for word in new_sen:
		if len(word) > len(largest):
			largest = word
			

	return word









#####################################################################
if __name__ == "__main__":
	print
	import doctest
	if doctest.testmod().failed == 0:
		print "*** ALL TESTS PASSED ***"
   