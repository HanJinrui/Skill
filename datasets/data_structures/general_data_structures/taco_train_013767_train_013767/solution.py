def getFloorAndCeil(arr, n, x):
	f = -1
	c = -1
	arr.sort()
	for i in arr:
		if i <= x:
			f = i
	for i in arr:
		if i >= x:
			c = i
			break
	return (f, c)
