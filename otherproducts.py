import numpy as np
def other_products(lst):
	""" have the function OtherProducts(arr) take the array of numbers stored in arr and return a new list of the 
	products of all the other numbers in the array for each element. For example: if arr is [1, 2, 3, 4, 5] then the 
	new array, where each location in the new array is the product of all other elements, is [120, 60, 40, 30, 24]. 
	The following calculations were performed to get this answer: [(2*3*4*5), (1*3*4*5), (1*2*4*5), (1*2*3*5), (1*2*3*4)]. 
	You should generate this new array and then return the numbers as a string joined by a hyphen: 120-60-40-30-24. The array 
	will contain at most 10 elements and at least 1 element of only positive integers. 
	Example::
	>>> other_products([1,4,3])
	'12-3-4'
	>>> other_products([3,1,2,6])
	'12-36-18-6'
	"""
	products = ''

	product_checker = lst

	for num in lst:
		product = np.product(product_checker)
		product = product / num
		products += str(product) + '-'
		
	return products[:-1]

		


		


#####################################################################
if __name__ == "__main__":
	print
	import doctest
	if doctest.testmod().failed == 0:
		print "*** ALL TESTS PASSED ***"
     