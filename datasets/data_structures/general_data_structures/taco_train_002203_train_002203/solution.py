def findEquilibrium(a, n):
	s = sum(a)
	s1 = 0
	for i in range(n):
		if s - s1 - a[i] == s1:
			return i
		s1 += a[i]
	return -1
