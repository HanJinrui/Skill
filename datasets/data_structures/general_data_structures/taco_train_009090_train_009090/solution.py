def max_adjacent_sum(a, n):
	b = []
	for i in range(n - 1):
		b.append(arr[i] + arr[i + 1])
	return max(b)
