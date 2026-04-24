class Solution:

	def countPairs(self, n, arr, k):
		l = [0] * k
		c = 0
		for i in arr:
			c += l[i % k]
			l[i % k] += 1
		return c
