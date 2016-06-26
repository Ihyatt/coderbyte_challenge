def time_convert(num):
	"""take the num parameter being passed and return the number of hours and minutes the parameter converts to 
	(ie. if num = 63 then the output should be 1:3). Separate the number of hours and minutes with a colon

	Example::
	>>> time_convert(126)
	'2:6'
	>>> time_convert(45)
	'0:45'

	"""
	hr = num / 60
	mins = num % 60

	return str(hr) + ":" + str(mins)


#####################################################################
if __name__ == "__main__":
	print
	import doctest
	if doctest.testmod().failed == 0:
		print "*** ALL TESTS PASSED ***"
   
