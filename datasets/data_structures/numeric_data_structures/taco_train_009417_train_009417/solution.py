def countPairs(a, n):
	return a.count(max(a)) * a.count(min(a)) if n > 1 else 0
