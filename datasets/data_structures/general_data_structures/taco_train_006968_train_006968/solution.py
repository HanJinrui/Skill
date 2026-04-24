class Solution:

	def kthElement(self, arr1, arr2, n, m, k):
		return sorted(arr1 + arr2)[k - 1]
