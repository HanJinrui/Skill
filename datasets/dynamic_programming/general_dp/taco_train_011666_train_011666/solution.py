class Solution:

	def minTimeForWritingChars(self, N, I, D, C):
		dp = [0] * (N + 1)
		dp[1] = I
		for i in range(2, N + 1):
			dp[i] = dp[i - 1] + I
			if i % 2 == 0:
				dp[i] = min(dp[i], dp[i // 2] + C)
			else:
				dp[i] = min(dp[i], dp[i // 2 + 1] + C + D)
		return dp[-1]
