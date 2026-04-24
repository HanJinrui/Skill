class Solution:

	def countKdivPairs(self, arr, n, k):
		d = [0 for i in range(k)]
		c = 0
		for i in range(n):
			r = arr[i] % k
			c += d[(k - r) % k]
			d[r] += 1
		return c
