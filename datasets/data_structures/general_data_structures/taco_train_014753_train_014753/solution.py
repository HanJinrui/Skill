class Solution:

	def lenOfLongIncSubArr(self, a, n):
		g = 1
		c = 0
		for i in range(1, n):
			if int(a[i - 1]) < int(a[i]):
				c = c + 1
				g = max(g, c + 1)
			else:
				c = 0
		return g
