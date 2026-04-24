class Solution:

	def distinctCount(self, arr, n):
		return len(set(map(abs, arr)))
