def minOps(a, n):
	j = n
	for i in range(n - 1, -1, -1):
		if a[i] == j:
			j -= 1
	return j
