class Solution:

	def countPS(self, string):
		S = string
		n = len(S)
		dp = [[0] * n for i in range(n)]
		M = 10 ** 9 + 7
		for i in range(n):
			for j in range(i, -1, -1):
				if i == j:
					dp[j][i] = 1
				elif S[i] == S[j]:
					dp[j][i] = dp[j + 1][i] + dp[j][i - 1] + 1
				else:
					dp[j][i] = dp[j + 1][i] + dp[j][i - 1] - dp[j + 1][i - 1]
		return dp[0][n - 1] % M
