class Solution:

	def totalCount(self, arr, n, k):
		return sum([elem // k + (1 if elem % k != 0 else 0) for elem in arr])
