class Solution:

	def superPrimes(self, n):
		p = [1] * (n + 1)
		for i in range(2, (n + 1) // 2):
			if p[i]:
				j = 2
				while i * j < n + 1:
					p[i * j] = 0
					j += 1
		c = 0
		for i in range(5, n + 1):
			if p[i] and p[i - 2]:
				c += 1
		return c
