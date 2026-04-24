class Solution:

	def TotalWays(self, str):
		s1 = str
		s2 = 'GEEKS'
		n = len(str)
		m = 10 ** 9 + 7
		dp = [[0] * 6 for ele in range(n + 1)]
		dp[0][0] = 1
		for i in range(n + 1):
			dp[i][0] = 1
		for i in range(1, n + 1):
			for j in range(1, 6):
				dp[i][j] = dp[i - 1][j]
				if s1[i - 1] == s2[j - 1]:
					dp[i][j] += dp[i - 1][j - 1] % m
		return dp[n][5] % m
