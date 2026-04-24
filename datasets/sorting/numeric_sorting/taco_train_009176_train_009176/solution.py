class Solution:

	def sortArray(self, arr, n, A, B, C):
		return sorted([A * x * x + b * x + C for x in arr])
