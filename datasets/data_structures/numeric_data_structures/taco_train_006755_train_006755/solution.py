class Solution:

	def maxDistance(self, arr, n):
		a = [x - i for (i, x) in enumerate(arr)]
		b = [x + i for (i, x) in enumerate(arr)]
		return max(max(a) - min(a), max(b) - min(b))
