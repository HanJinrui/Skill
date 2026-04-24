class Solution:

	def minTime(self, a, b, n):
		for i in range(1, n, 2):
			(a[i], b[i]) = (b[i], a[i])
		return min(sum(a), sum(b))
