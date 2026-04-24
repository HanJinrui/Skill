def kthDiff(a, n, k):
	diff = []
	for i in range(n):
		for j in range(i + 1, n):
			diff.append(abs(a[i] - a[j]))
	return sorted(diff)[k - 1]
