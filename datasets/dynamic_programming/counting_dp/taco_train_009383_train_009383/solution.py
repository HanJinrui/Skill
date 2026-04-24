class Solution:

	def uniquePaths(self, m, n):
		a = m - 1
		b = n - 1
		ret = 1
		for i in range(b):
			ret = ret * (a + b - i) / (b - i)
		return round(ret)
