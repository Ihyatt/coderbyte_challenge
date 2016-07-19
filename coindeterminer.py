def coin_deter(num):
	"""have the function CoinDeterminer(num) take the input, which will be an integer ranging from 1 to 250, 
	and return an integer output that will specify the least number of coins, that when added, equal the input integer. 
	Coins are based on a system as follows: there are coins representing the integers 1, 5, 7, 9, and 11. So for example: if num is 16, 
	then the output should be 2 because you can achieve the number 16 with the coins 9 and 7. If num is 25, then the output should be 3 
	because you can achieve 25 with either 11, 9, and 5 coins or with 9, 9, and 7 coins. 
	Example::

	>>> coin_deter(6)
	2
	>>> coin_deter(16)
	2
	"""
	if num < 5:
		return num 

	count = 1
	while num - 11 > 0:
		count += 1
		num -= 11

	if num % 2 == 0:
		count += 1

	return count


#####################################################################
if __name__ == "__main__":
	print
	import doctest
	if doctest.testmod().failed == 0:
		print "*** ALL TESTS PASSED ***"
     
