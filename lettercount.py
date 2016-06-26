
def freq_check(word):
	freq = {}
	count = 1
	for letter in word:
		if letter not in freq:
			freq[letter] = 1
		else:
			freq[letter] += 1
	for letter in freq:
		if freq[letter] > count:
			count = freq[letter]

	return count

def letter_count(str):
	"""take the str parameter being passed and return the first word with the greatest number 
	of repeated letters. For example: "Today, is the greatest day ever!" should return greatest 
	because it has 2 e's (and 2 t's) and it comes before ever which also has 2 e's. 
	If there are no words with repeating letters return -1. Words will be separated by spaces. 
	Example::
	>>> letter_count('Hello apple pie')
	'Hello'

	>>> letter_count("No words")
	-1

	"""
	count = 1

	rep_letter_word = None
	sen = str.split(" ")
	for word in sen: 
		if freq_check(word) > count:
			count = freq_check(word)
			rep_letter_word = word
		

	return rep_letter_word or -1
	

#####################################################################
if __name__ == "__main__":
	print
	import doctest
	if doctest.testmod().failed == 0:
		print "*** ALL TESTS PASSED ***"
     