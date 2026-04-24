def findDifference(a1, a2, n):
	c = 0
	for i in range(n):
		j = i + 1
		while a1[i] != a2[i]:
			c += 1
			(a1[i], a1[j]) = (a1[j], a1[i])
			j += 1
	return c
