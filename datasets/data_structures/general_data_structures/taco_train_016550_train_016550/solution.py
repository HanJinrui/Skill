class Solution:

	def minSum(self, a, b, n):
		c = sorted(a)
		d = sorted(b)
		if a.index(c[0]) != b.index(d[0]):
			return c[0] + d[0]
		else:
			return min(c[0] + d[1], d[0] + c[1])
