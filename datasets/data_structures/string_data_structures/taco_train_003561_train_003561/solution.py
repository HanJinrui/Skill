def primeOccurences(arr, n, k):
	d = {}
	for i in arr:
		d[i] = 1 + d.get(i, 0)

	def helper(x):
		if x == 1:
			return False
		for i in range(2, int(x ** 0.5) + 1):
			if x % i == 0:
				return False
		return True
	ans = []
	for i in d:
		if d[i] >= k and helper(d[i]):
			ans.append(i)
	if not ans:
		return [-1]
	return sorted(ans)
