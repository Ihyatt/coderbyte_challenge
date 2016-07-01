def counting_mins(string):
	""" take the str parameter being passed which will be two times 
	(each properly formatted with a colon and am or pm) separated by a 
	hyphen and return the total number of minutes between the two times. 
	The time will be in a 12 hour clock format. For example: if str is 9:00am-10:00am 
	then the output should be 60. If str is 1:00pm-11:00am the output should be 1320.

	Example::
	>>> counting_mins("12:30pm-12:00am")
	690

	>>> counting_mins("1:23am-1:08am")
	1425

	"""

	times = string.split("-")
	first_time = times[0]
	second_time = times[1]
	time_range = 0 

	if first_time[-2:] == "pm" and first_time[:2] == "12":
		first_time_hour_to_min = int(first_time[:-5]) * 60
		first_time_min = int(first_time[-4:-2])
		first_time = first_time_hour_to_min + first_time_min

	elif first_time[-2:] == "pm" and first_time[:2] != "12":
		first_time_hour_to_min = (int(first_time[:-5]) + 12) * 60
		first_time_min = int(first_time[-4:-2])
		first_time = first_time_hour_to_min + first_time_min

	elif first_time[-2:] == "am" and first_time[:2] == "12":
		first_time_hour_to_min = (int(first_time[:-5]) + 12) * 60
		first_time_min = int(first_time[-4:-2])
		first_time = first_time_hour_to_min + first_time_min

	else: 
		first_time_hour_to_min = int(first_time[:-5]) * 60
		first_time_min = int(first_time[-4:-2])
		first_time = first_time_hour_to_min + first_time_min

	if second_time[-2:] == "pm" and second_time[:2] == "12":
		second_time_hour_to_min = int(second_time[:-5]) * 60
		second_time_min = int(second_time[-4:-2])
		second_time = second_time_hour_to_min + second_time_min

	elif second_time[-2:] == "pm" and second_time[:2] != "12":
		second_time_hour_to_min = (int(second_time[:-5]) + 12) * 60
		second_time_min = int(second_time[-4:-2])
		second_time = second_time_hour_to_min + second_time_min

	elif second_time[-2:] == "am" and second_time[:2] == "12":
		second_time_hour_to_min = (int(second_time[:-5]) + 12) * 60
		second_time_min = int(second_time[-4:-2])
		second_time = second_time_hour_to_min + second_time_min
	else:
		second_time_hour_to_min = int(second_time[:-5]) * 60
		second_time_min = int(second_time[-4:-2])
		second_time = second_time_hour_to_min + second_time_min


	if first_time > second_time:
		time_range = 1440 - first_time + second_time
	elif first_time == second_time:
		time_range = 0 
	else: 
		time_range = second_time - first_time

	return time_range



		
	

#####################################################################
if __name__ == "__main__":
	print
	import doctest
	if doctest.testmod().failed == 0:
		print "*** ALL TESTS PASSED ***"