def findElement(arr, n):
	maxi = arr[0]
	for i in range(1, n - 1):
		maxi = max(maxi, arr[i])
		if maxi <= arr[i] and min(arr[i + 1:]) >= arr[i]:
			return arr[i]
	return -1
