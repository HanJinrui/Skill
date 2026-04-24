class Solution:

	def subCount(self, arr, n, k):
		h = {0: 1}
		c = 0
		summ = 0
		for i in arr:
			summ += i
			r = summ % k
			if r in h:
				c += h[r]
				h[r] += 1
			else:
				h[r] = 1
		return c
