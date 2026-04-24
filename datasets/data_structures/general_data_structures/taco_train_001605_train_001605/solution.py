class Solution:

	def maxVal(self, a, n):
		for i in range(n):
			a[i] = a[i] - i
		return max(a) - min(a)
