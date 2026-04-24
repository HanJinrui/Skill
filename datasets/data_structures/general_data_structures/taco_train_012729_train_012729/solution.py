import numpy as np

def findMaxProduct(arr, n, m):
	res = 1
	for i in range(n - m + 1):
		res = max(res, np.prod(arr[i:i + m]))
	return res
