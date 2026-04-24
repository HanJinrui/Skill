def kthSmallest(mat, n, k):
	l = sum(mat, [])
	l.sort()
	return l[k - 1]
