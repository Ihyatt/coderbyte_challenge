def run_length(astring):
	""" have the function RunLength(str) take the str parameter 
	being passed and return a compressed version of the string using
	the Run-length encoding algorithm. This algorithm works by taking 
	the occurrence of each repeating character and outputting that number 
	along with a single character of the repeating sequence. For example: 
	"wwwggopp" would return 3w2g1o2p. The string will not contain any numbers, 
	punctuation, or symbols.
	Example::
	>>> run_length("aabbcde")
	'2a2b1c1d1e'
	>>> run_length("wwwbbb")
	'3w3b'
	"""
	counted_letters = ""

	count = 1
	current_letter = astring[0]
	for letter in astring[1:]:
		if letter != current_letter:

			counted_letters += str(count) + current_letter
			current_letter = letter
			count = 1
		else: 
			count += 1

	return counted_letters + str(count) + current_letter




#####################################################################
if __name__ == "__main__":
	print
	import doctest
	if doctest.testmod().failed == 0:
		print "*** ALL TESTS PASSED ***"
