def findMinimumInvertingFactor(arr, n):
	x = [int(str(i)[::-1]) for i in arr]
	x.sort()
	d = 99999
	for k in range(n - 1):
		a = abs(x[k] - x[k + 1])
		if a < d:
			d = a
	return d
