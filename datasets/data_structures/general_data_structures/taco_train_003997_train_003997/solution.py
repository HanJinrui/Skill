def Max_Sum(arr, n, k):
	arr.sort()
	i = 0
	j = n - 1
	m = [0, 0]
	while i < j:
		if arr[j] + arr[i] < k:
			if m[1] + m[0] < arr[j] + arr[i]:
				m = [arr[i], arr[j]]
			i += 1
		else:
			j -= 1
	return m
