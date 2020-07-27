def quickSort(array, start=0, end=None):
	if len(array) < 2:
		return array
	if end is None:
		end = len(array)-1
	if end <= 0 or start >= len(array) or start >= end:
		return array
	p, l, r = start, start+1, end	
	# [6 5 2 3 5 8 9]
	#  p         r l	
	while l <= r:
		if array[r] < array[p] < array[l]:
			array[r], array[l] = array[l], array[r]
		if array[l] <= array[p]:
			l += 1
		if array[r] >= array[p]:
			r -= 1
	# swap right & pivot
	array[r], array[p] = array[p], array[r]
	# split array on the right index.		
	quickSort(array, start, r-1) # left: start, right-1
	quickSort(array, r+1, end) # right: right+1, end	
	return array
	
		