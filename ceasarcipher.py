import string
def word_change(word,shift):
	new_word = ""
	alpha_checker = list(string.ascii_lowercase)
	alpha_checker_upper = list(string.ascii_uppercase)
	

	for letter in word:
		if letter in alpha_checker: 
			found_index = alpha_checker.index(letter)
			new_index = (found_index + shift) % 26
			new_letter = alpha_checker[new_index]
			new_word += new_letter
		elif letter in alpha_checker_upper:
			found_index = alpha_checker_upper.index(letter)
			new_index = (found_index + shift) % 26
			new_letter = alpha_checker_upper[new_index]
			new_word += new_letter

	return new_word




def ceasar_cipher(string,shift):
	""" have the function CaesarCipher(str,num) take the str parameter and perform a 
	Caesar Cipher shift on it using the num parameter as the shifting number. A Caesar
	Cipher works by shifting each letter in the string N places down in the alphabet (in 
	this case N will be num). Punctuation, spaces, and capitalization should remain intact. 
	For example if the string is "Caesar Cipher" and num is 2 the output should be 'Ecguct 
	Ekrjgt'. 

	Example::
	>>> ceasar_cipher('Hello', 4)
	'Lipps'

	>>> ceasar_cipher('abc', 0)
	'abc'

	"""
	new_words = []
	set_of_strings = string.split(" ")
	for word in set_of_strings:
		new_words.append(word_change(word, shift))

	new_str = " ".join(new_words)

	return new_str


#####################################################################
if __name__ == "__main__":
	print
	import doctest
	if doctest.testmod().failed == 0:
		print "*** ALL TESTS PASSED ***"
