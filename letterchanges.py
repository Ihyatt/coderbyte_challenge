import string
def word_change(word):
	new_word = ""
	alpha_checker = list(string.ascii_lowercase)
	vowels = ["a","e","i","o","u"]

	for letter in word:
		if letter.isalpha():
			found_index = alpha_checker.index(letter)
			new_index = (found_index + 1) % 26
			new_letter = alpha_checker[new_index]
			if new_letter in vowels:
				new_letter = new_letter.upper()
			new_word += new_letter
		else:
			new_word += letter

	return new_word




def letter_changes(str):
	""" take the str parameter being passed and modify it using the following algorithm. 
	Replace every letter in the string with the letter following it in the alphabet 
	(ie. c becomes d, z becomes a). Then capitalize every vowel in this new string (a, e, i, o, u)
	and finally return this modified string. 

	Example::
	>>> letter_changes('hello*3')
	'Ifmmp*3'

	>>> letter_changes('fun times!')
	'gvO Ujnft!'

	"""
	new_words = []
	set_of_strings = str.split(" ")
	for word in set_of_strings:
		new_words.append(word_change(word))

	new_str = " ".join(new_words)

	return new_str









#####################################################################
if __name__ == "__main__":
	print
	import doctest
	if doctest.testmod().failed == 0:
		print "*** ALL TESTS PASSED ***"
   

