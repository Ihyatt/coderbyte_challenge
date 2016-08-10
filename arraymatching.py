def array_matching(lst):
	"""Using the Python language, have the function ArrayMatching(strArr) read the array of strings 
	stored in strArr which will contain only two elements, both of which will represent an array of 
	positive integers. For example: if strArr is ["[1, 2, 5, 6]", "[5, 2, 8, 11]"], then both elements 
	in the input represent two integer arrays, and your goal for this challenge is to add the elements 
	in corresponding locations from both arrays. For the example input, your program should do the following 
	additions: [(1 + 5), (2 + 2), (5 + 8), (6 + 11)] which then equals [6, 4, 13, 17]. Your program should 
	finally return this resulting array in a string format with each element separated by a hyphen: 6-4-13-17. 
	Example::
	>>> array_matching(["[5, 2, 3]", "[2, 2, 3, 10, 6]"])
	'7-4-6-10-6'
	>>> array_matching(["[1, 2, 1]", "[2, 1, 5, 2]"])
	'3-3-6-2'
	"""

	first = lst[0]
	second = lst[1]

	first_num = []
	second_num = []
	final_num = []


	first = first.split(',')
	first[0] = first[0][1:]
	first[-1] = first[-1][:-1]
	
	second = second.split(',')
	
	second[0] = second[0][1:]
	second[-1] = second[-1][:-1]

	

	for num in first:
		first_num.append(int(num))

	for num in second:
		second_num.append(int(num))

	while len(first_num) > 0:
		new_num = first_num[0] + second_num[0]
		final_num.append(new_num)
		first_num.pop(0)
		second_num.pop(0)

	final_num.extend(first_num)
	final_num.extend(second_num)

	
	
	return "-".join(map(str, final_num))

	
	


#####################################################################
if __name__ == "__main__":
	print
	import doctest
	if doctest.testmod().failed == 0:
		print "*** ALL TESTS PASSED ***"
