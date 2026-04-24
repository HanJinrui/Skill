def largestSum(arr, n):
	k = arr[0]
	mx = arr[0]
	for i in range(1, n):
		if arr[i] > arr[i - 1]:
			k += arr[i]
			mx = max(mx, k)
		else:
			k = arr[i]
	return mx
