class Solution:

	def required(self, a, n, k):
		g = max(a)
		if g > k:
			return g - k
		return -1
