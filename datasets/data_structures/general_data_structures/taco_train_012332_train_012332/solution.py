def findZeroes(arr, n, m):
	a = 0
	j = 0
	for i in range(len(arr)):
		if arr[i] == 0:
			a += 1
		if a > m:
			if arr[j] == 0:
				a -= 1
			j += 1
	return n - j
