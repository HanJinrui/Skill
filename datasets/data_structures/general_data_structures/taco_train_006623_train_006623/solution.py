def Rearrange(arr, n):
	res = [-1] * n
	for i in arr:
		if i != -1:
			res[i] = i
	return res
