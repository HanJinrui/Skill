class Solution:

	def arrangeTiles(self, N):
		dp = [1] * (N + 1)
		for i in range(4, N + 1):
			dp[i] = dp[i - 1] + dp[i - 4]
		return dp[N]
