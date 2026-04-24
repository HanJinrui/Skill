class Solution:

	def maxTripletSum(self, arr, n, K):
		s = set(arr)
		return min(len(s), n - K)
