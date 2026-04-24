class Solution:

	def maxSubarrayXOR(self, n, arr):
		dp = [1]
		for i in range(n):
			dp.append(max(dp[-1] ^ arr[i], arr[i]))
		return max(dp)
