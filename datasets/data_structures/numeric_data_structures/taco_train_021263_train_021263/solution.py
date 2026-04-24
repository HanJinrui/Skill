def countSubsets(a, n):
	s = set([x for x in a if x % 2 == 0])
	return pow(2, len(s)) - 1
