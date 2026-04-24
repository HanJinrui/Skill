def minAnd2ndMin(a, n):
	ans = sorted(set(a))
	if len(ans) >= 2:
		return ans[:2]
	return [-1, -1]
