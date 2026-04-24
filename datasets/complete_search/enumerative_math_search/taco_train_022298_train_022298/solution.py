def getCandidate(n, k):
	i = k
	while i * k <= n:
		i *= k
	return i
