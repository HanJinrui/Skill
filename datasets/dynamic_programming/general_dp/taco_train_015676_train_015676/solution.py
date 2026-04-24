class Solution:

	def count(self, N):
		dp = [[0] * 10 for i in range(N)]
		for i in range(10):
			dp[0][i] = 1
			if i != 0:
				dp[0][i] += dp[0][i - 1]
		for i in range(1, N):
			for j in range(10):
				dp[i][j] = dp[i - 1][j]
				if j != 0:
					dp[i][j] += dp[i][j - 1]
		return dp[N - 1][9]
