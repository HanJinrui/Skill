class Solution:

	def minSteps(self, m, n, d):
		if d == m or d == n:
			return 1
		if m == n:
			return -1
		k = m
		c = 2
		c1 = 0
		c2 = 0
		while k:
			if d == k:
				c1 = c
				break
			if k < m:
				c += 4
			else:
				c += 2
			k += m
			if k >= n:
				k -= n
		if not c1:
			return -1
		k = n - m
		c = 2
		while k:
			if d == k:
				c2 = c
			c += 2
			k -= m
			if k < 0:
				c += 2
				k += n
		return min(c1, c2)
