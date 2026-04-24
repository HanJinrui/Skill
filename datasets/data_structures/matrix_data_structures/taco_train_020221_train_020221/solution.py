def findK(arr, n, m, k):
	res = []
	while arr:
		res.extend(arr.pop(0))
		arr = list(zip(*arr))[::-1]
	return res[k - 1]
