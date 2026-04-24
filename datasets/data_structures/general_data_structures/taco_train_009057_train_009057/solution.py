def KthMissingElement(l, n, k):
	for i in range(0, n - 1):
		diff = l[i + 1] - l[i]
		if diff > k:
			return l[i] + k
		k -= diff - 1
	return -1
