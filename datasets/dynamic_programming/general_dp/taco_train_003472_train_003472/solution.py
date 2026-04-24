class Solution:

	def minAmount(self, a, n):
		for i in range(2, n):
			a[i] = min(a[i - 2], a[i - 1]) + a[i]
		return min(a[-1], a[-2])
