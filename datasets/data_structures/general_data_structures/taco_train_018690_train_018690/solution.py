def ReducingWalls(arr, n, k):
	return sum([(each - 1) // k for each in arr if each > k])
