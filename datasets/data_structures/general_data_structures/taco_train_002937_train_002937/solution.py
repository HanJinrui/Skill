class Solution:

	def reverseInGroups(self, arr, N, K):
		for i in range(0, N, K):
			arr[i:i + K] = arr[i:i + K][::-1]
