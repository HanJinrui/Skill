class Solution:

	def possible(self, arr, n):
		return sum(arr) == n * (n + 1) // 2
