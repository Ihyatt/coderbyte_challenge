def letter_in_word_count(word):
	#returns number of times letter(s) are repeated as a count
	letter_freq = {}
	count = 0

	for letter in word:
		if letter in letter_freq:
			letter_freq[letter] += 1
		else:
			letter_freq[letter] = 1 
	

	for letter in letter_freq:
		if letter_freq[letter] > 1:
			count += 1

	return count



def letter_count(string):
	"""have the function LetterCount(str) take the str 
	parameter being passed and return the first word with 
	the greatest number of repeated letters. For example: "Today, 
	is the greatest day ever!" should return greatest because it 
	has 2 e's (and 2 t's) and it comes before ever which also has 
	2 e's. If there are no words with repeating letters return -1. 
	Words will be separated by spaces.

	Example::
	>>> letter_count("Hello apple pie")
	'Hello'
	>>> letter_count("No words") 
	-1
	"""

	count = 0 
	repeat = ""
	words = string.split()
	for word in words:
		if letter_in_word_count(word) > count:
			repeat = word
			count = letter_in_word_count(word)
	if repeat == "":
		return - 1
	else: 
		return repeat


#####################################################################
if __name__ == "__main__":
	print
	import doctest
	if doctest.testmod().failed == 0:
		print "*** ALL TESTS PASSED ***"





