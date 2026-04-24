from math import factorial

def getAnswer(arr, n, k, x):
	arr.sort()
	count = 0
	f = factorial(k - 1)
	j = k - 1
	for i in range(n - k + 1):
		while j < n and arr[j] - arr[i] <= x:
			j += 1
		if j - i >= k and arr[j - 1] - arr[i] <= x:
			count += factorial(j - i - 1) // f // factorial(j - i - k)
	return count % (10 ** 9 + 7)
