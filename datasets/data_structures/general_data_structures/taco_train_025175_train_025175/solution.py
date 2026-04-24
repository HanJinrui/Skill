def getTriangle(arr, n):
	l = arr
	for i in range(n):
		l = [l[i] + l[i + 1] for i in range(len(l) - 1)]
		arr[:0] = l
	return arr
