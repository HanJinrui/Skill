class Solution:

	def minSteps(self, n):
		dp = [0] * (N + 1)
		for i in range(2, N + 1):
			dp[i] = dp[i - 1] + 1
			for j in range(2, 4):
				if i % j == 0:
					dp[i] = min(dp[i], dp[i // j] + 1)
		return dp[N]
