from math import ceil
def formatted_division(num1, num2):
	"""have the function FormattedDivision(num1,num2) take both parameters 
	being passed, divide num1 by num2, and return the result as a string with 
	properly formatted commas and 4 significant digits after the decimal place. 
	For example: if num1 is 123456789 and num2 is 10000 the output should be "12,345.6789". 
	The output must contain a number in the one's place even if it is a zero
	Example::
	>>> formatted_division(2,3)
	'0.6667'
	>>> formatted_division(10, 10)
	'1.0000'
	>>> formatted_division(123456789, 10000)
	'12,345.6789'
	"""

	div = (1.0 * num1) / num2

	div_round = round(div,4)
	div_round = str(div_round)
	decimal = div_round.index('.')
	decimal_string = div_round[decimal:]
	if len(decimal_string) < 3: 
		decimal_string += '000'
	elif len(decimal_string) < 4:
		decimal_string += '00'
	elif len(decimal_string) < 5:
		decimal_string += '0'

	full_num = div_round[:decimal]

	rev_num = ""
	count = 0 
	for num in reversed(full_num):
		count += 1
		if count == 3:
			rev_num += num + ','
			count = 0 
		else: 
			rev_num +=  num
	return rev_num[::-1] + decimal_string








#####################################################################
if __name__ == "__main__":
	print
	import doctest
	if doctest.testmod().failed == 0:
		print "*** ALL TESTS PASSED ***"