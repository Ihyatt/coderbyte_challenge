def basic_numerals(string):
	"""have the function BasicRomanNumerals(str) read str which will be a string of Roman numerals. The numerals being used are: 
	I for 1, V for 5, X for 10, L for 50, C for 100, D for 500 and M for 1000. In Roman numerals, to create a number like 11 you 
	simply add a 1 after the 10, so you get XI. But to create a number like 19, you use the subtraction notation which is to add 
	an I before an X or V (or add an X before an L or C). So 19 in Roman numerals is XIX. 

	The goal of your program is to return the decimal equivalent of the Roman numeral given. For example: if str is "XXIV" your 
	program should return 24

	Example::
	>>> basic_numerals("IV")
	4

	>>> basic_numerals("XLVI")
	46

	"""
	numerals = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

	result = 0 

	idx = 1
	while idx < len(string):

		current = string[idx]
		previous = string[idx - 1]
		if numerals[previous] < numerals[current]:
			result -= numerals[previous]
			
		else: 
			result += numerals[previous]
			

		if idx == len(string) - 1:
			result += numerals[current]


		idx += 1

	return result


#####################################################################
if __name__ == "__main__":
	print
	import doctest
	if doctest.testmod().failed == 0:
		print "*** ALL TESTS PASSED ***"