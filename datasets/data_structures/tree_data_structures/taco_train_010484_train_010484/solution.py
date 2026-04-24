class Solution:

	def findHeight(self, N, arr):
		dp = [0] * N
		for i in range(N):
			dp[i] = dp[arr[i]] + 1
		return dp[N - 1]
