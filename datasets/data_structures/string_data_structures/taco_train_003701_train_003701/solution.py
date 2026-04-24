class Solution:

	def findSwapValues(self, a, n, b, m):
		g = sum(a) - sum(b)
		a = set(a)
		b = set(b)
		for i in a:
			if (2 * i - g) / 2 in b:
				return 1
		return -1
