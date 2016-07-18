def letter_swap(word):
	
	letters = [] 
		
	swapped_word = ''
	index = []
	num = None

	if word[0].isalpha() or len(word) < 3:
		swapped_word = word.swapcase()
		return swapped_word


	for char in word: 
		if char.isdigit():
			index.append(word.index(char))
	

	if len(index) == 2:
		if word[index[0] + 1 : index[1]].isalpha():
			
			num1 =  word[index[0]]
			
			
			num2 = word[index[1]]
			
			letters = list(word)
			

			letters[index[0]] = num2
			
			letters[index[1]] = num1
			

			full_word = ''.join(letters)
			

			swapped_word = full_word.swapcase()
			return swapped_word





def swapii(string):
	"""Have the function SwapII(str) take the str parameter and swap the case of 
	each character. Then, if a letter is between two numbers (without separation), 
	switch the places of the two numbers. For example: if str is "6Hello4 -8World, 7 yes3" 
	the output should be 4hELLO6 -8wORLD, 7 YES3.
	Example::
	>>> swapii('Hello -5LOL6')
	'hELLO -6lol5'

	>>> swapii('2S 6 du5d4e')
	'2s 6 DU5D4E'
	"""
	


	swapped = []
	words = string.split()

	for word in words:
		swapped.append(letter_swap(word))
	swapped = ' '.join(swapped)

	
	return swapped


#####################################################################
if __name__ == "__main__":
	print
	import doctest
	if doctest.testmod().failed == 0:
		print "*** ALL TESTS PASSED ***"
