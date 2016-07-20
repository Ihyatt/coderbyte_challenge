def most_free_time(lst):
	"""have the function MostFreeTime(strArr) read the strArr parameter being passed which will 
	represent a full day and will be filled with events that span from time X to time Y in the day. 
	The format of each event will be hh:mmAM/PM-hh:mmAM/PM. For example, strArr may be ["10:00AM-12:30PM",
	"02:00PM-02:45PM","09:10AM-09:50AM"]. Your program will have to output the longest amount of free time 
	available between the start of your first event and the end of your last event in the format: hh:mm. The 
	start event should be the earliest event in the day and the latest event should be the latest event in the day. 
	The output for the previous input would therefore be 01:30 (with the earliest event in the day starting at 09:10AM 
	and the latest event ending at 02:45PM). The input will contain at least 3 events and the events may be out of 
	order.
	Example::
	>>> most_free_time(["12:15PM-02:00PM","09:00AM-10:00AM","10:30AM-12:00PM"])
	'00:30'

	>>> most_free_time(["12:15PM-02:00PM","09:00AM-12:11PM","02:02PM-04:00PM"])
	'00:04'
	"""

	times = []
	for time in lst:
		split_time = time.split('-')
		times.append(split_time)

	min_times = [] 
	for time_set in times:
		for time in time_set:
			if time[-2:] == 'PM':
				if time[:2] == '12':
					time = (12 * 60) + int(time[-4:-2])
					min_times.append(time)
				
				else:
					time = (int(time[:2]) + 12) * 60 + int(time[-4:-2])
					min_times.append(time)
					
			else:
				if time[:2] == '12':
					time = int(time[-4:-2])
					min_times.append(time)
					
				else:
					time = (int(time[:2]) * 60) + int(time[-4:-2])
					min_times.append(time)
					

		
	new_min_times = []

	idx = 0
	while idx < len(min_times) - 1:
		new_min_times.append([min_times[idx], min_times[idx + 1]])
		idx += 2
		
	new_min_times = sorted(new_min_times)
	
	

	most_time = 0 

	end_activity = new_min_times[0][1]
	
	for time_sets in new_min_times[1:]:
		free_time = time_sets[0] - end_activity
		
		if free_time > most_time:
			most_time = free_time
		end_activity = time_sets[1]
	

	return '%02i:%02i' % (most_time // 60, most_time % 60)




#####################################################################
if __name__ == "__main__":
	print
	import doctest
	if doctest.testmod().failed == 0:
		print "*** ALL TESTS PASSED ***"
