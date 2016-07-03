def rectangle_area(lst):
	""" RectangleArea(strArr) take the array of strings stored in strArr, 
	which will only contain 4 elements and be in the form (x y) where x and y 
	are both integers, and return the area of the rectangle formed by the 4 points 
	on a Cartesian grid. The 4 elements will be in arbitrary order. For example: if 
	strArr is ["(0 0)", "(3 0)", "(0 2)", "(3 2)"] then your program should return 6 
	because the width of the rectangle is 3 and the height is 2 and the area of a rectangle 
	is equal to the width * height. 

	Example::
	>>> rectangle_area(["(1 1)","(1 3)","(3 1)","(3 3)"])
	4
	>>> rectangle_area(["(0 0)","(1 0)","(1 1)","(0 1)"])
	1

	"""
	rect = []

	for quadrant in lst:
		rect.append([int(quadrant[1]), int(quadrant[-2])])
	

	width = rect[0][0] + rect[1][0]
	height = rect[0][1] + rect[2][1]

	area = width * height

	return area

#####################################################################
if __name__ == "__main__":
	print
	import doctest
	if doctest.testmod().failed == 0:
		print "*** ALL TESTS PASSED ***"
     