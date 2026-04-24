import math

def minMoves(a, n, k):
	count = 0
	for i in range(1, n):
		if a[i] > a[i - 1]:
			diff = a[i] - a[i - 1]
			div = math.ceil(diff / k)
			count += div
			a[i] = a[i] - k * div
	return count % 1000000007
