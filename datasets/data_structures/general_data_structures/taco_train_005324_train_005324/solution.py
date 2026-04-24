def inversePermutation(a, n):
	b = [0] * n
	for i in range(n):
		b[a[i] - 1] = i + 1
	return b
