class Solution:

	def maxSumIS(self, arr, n):
		n = len(arr)
		dp = arr[:]
		for i in range(1, n):
			for j in range(0, i):
				if arr[j] < arr[i]:
					dp[i] = max(dp[i], dp[j] + arr[i])
		return max(dp)
