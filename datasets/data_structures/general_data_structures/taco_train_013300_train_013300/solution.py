class Solution:

	def mergeHeaps(self, a, b, n, m):
		c = a + b
		c.sort()
		c = c[::-1]
		return c
