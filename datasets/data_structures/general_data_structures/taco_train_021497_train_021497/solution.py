def multiply(arr, n):
	return sum(arr[:n // 2]) * sum(arr[n // 2:])
