def sum(arr, n):
	summ = 0
	for i in range(0, n):
		for j in range(i + 1, n):
			if abs(arr[j] - arr[i]) > 1:
				summ += arr[j] - arr[i]
	return summ
