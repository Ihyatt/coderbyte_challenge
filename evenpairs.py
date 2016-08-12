import re 
def even_pairs(str):
	"""have the function EvenPairs(str) take the str parameter being passed and determine 
	if a pair of adjacent even numbers exists anywhere in the string. If a pair exists, 
	return the string true, otherwise return false. For example: if str is "f178svg3k19k46" 
	then there are two even numbers at the end of the string, "46" so your program should 
	return the string true. Another example: if str is "7r5gg812" then the pair is "812" 
	(8 and 12) so your program should return the string true. 
	Example::
	>>> even_pairs("3gy41d216")
	True
	>>> even_pairs("f09r27i8e67")
	False
	"""
	evens = [0,2,4,6,8]
	nums = re.split('[a-z]+', str)

	for num in nums:
		if len(num) > 1:
			if int(num[-1]) % 2 == 0:
			
				for n in num[:-1]:
				
					if int(n) in evens:
						return True

	return False



#####################################################################
if __name__ == "__main__":
	print
	import doctest
	if doctest.testmod().failed == 0:
		print "*** ALL TESTS PASSED ***"
   