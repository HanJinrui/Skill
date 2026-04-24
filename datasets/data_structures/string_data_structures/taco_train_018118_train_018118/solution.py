def maximumFrequency(S):
	S = S.split(' ')
	d = dict()
	for i in S:
		d[i] = d.get(i, 0) + 1
	maxi = 0
	for i in S:
		if d[i] > maxi:
			maxi = d[i]
			c = i
	return c + ' ' + str(maxi)
