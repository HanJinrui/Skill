def maxPerimeter(arr, n):
	arr.sort()
	for i in reversed(range(n - 2)):
		if arr[i] + arr[i + 1] > arr[i + 2]:
			return arr[i] + arr[i + 1] + arr[i + 2]
	return -1
