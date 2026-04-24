class Solution:

	def formCoils(self, n):
		c = [2 * n * (4 * n + 1)]
		m = 1
		for i in range(2, 4 * n, 2):
			for _ in range(i):
				c.append(c[-1] - 4 * n * m)
			for _ in range(i):
				c.append(c[-1] + m)
			m *= -1
		for _ in range(4 * n - 1):
			c.append(c[-1] + 4 * n)
		return [c, [16 * n * n + 1 - x for x in c]]
