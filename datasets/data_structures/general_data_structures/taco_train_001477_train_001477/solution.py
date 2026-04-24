class Solution:

	def kLargest(self, arr, n, k):
		return sorted(arr)[::-1][:k]
