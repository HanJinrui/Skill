def dupLastIndex(arr, n):
	for x in range(1, n):
		if arr[-x] == arr[-x - 1]:
			return (n - x, arr[-x])
	return [-1]
