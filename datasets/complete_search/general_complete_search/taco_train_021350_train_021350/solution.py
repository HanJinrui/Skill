from bisect import bisect_left

class Solution:

	def searchInsertK(self, Arr, N, k):
		return bisect_left(Arr, k)
