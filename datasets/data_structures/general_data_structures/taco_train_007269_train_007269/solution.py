def MaxZero(arr, n):
	arr.sort(key=lambda i: (list(str(i)).count('0'), i), reverse=True)
	if list(str(arr[0])).count('0') == 0:
		return -1
	return arr[0]
