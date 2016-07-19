def stock_picker(lst):
	"""have the function StockPicker(arr) take the array of numbers stored in arr which will contain 
	integers that represent the amount in dollars that a single stock is worth, and return the maximum 
	profit that could have been made by buying stock on day x and selling stock on day y where y > x. For 
	example: if arr is [44, 30, 24, 32, 35, 30, 40, 38, 15] then your program should return 16 because at 
	index 2 the stock was worth $24 and at index 6 the stock was then worth $40, so if you bought the stock at 
	24 and sold it at 40, you would have made a profit of $16, which is the maximum profit that could have been 
	made with this list of stock prices. 
	Example::
	>>> stock_picker([10,12,4,5,9])
	5

	>>> stock_picker([14,20,4,12,5,11])
	8
	"""

	max_profit = 0 

	for buy_day in range(0, len(lst) - 1):
		for sell_day in range(buy_day, len(lst)):
			profit = lst[sell_day] - lst[buy_day]
			if profit > max_profit:
				max_profit = profit

	return max_profit

#####################################################################
if __name__ == "__main__":
	print
	import doctest
	if doctest.testmod().failed == 0:
		print "*** ALL TESTS PASSED ***"
