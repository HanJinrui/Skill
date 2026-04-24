class Solution:

	def countSubArrayProductLessThanK(self, a, n, k):
		c = 0
		p = 1
		(i, j) = (0, 0)
		if k == 1:
			return 0
		while j < n:
			p *= a[j]
			while p >= k:
				p //= a[i]
				i += 1
			c += j - i + 1
			j += 1
		return c
