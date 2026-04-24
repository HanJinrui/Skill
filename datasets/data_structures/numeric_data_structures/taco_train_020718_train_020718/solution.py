def getFreq(x, n):
	d = [0] * 10
	for j in range(1, n + 1):
		for k in str(x ** j):
			d[int(k)] += 1
	return d
