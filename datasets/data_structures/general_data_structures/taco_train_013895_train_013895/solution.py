def product(arr, n, mod):
	a = 1
	for i in arr:
		a *= i
	return a % mod
