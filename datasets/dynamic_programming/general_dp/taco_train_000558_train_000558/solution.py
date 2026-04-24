from math import inf

class Solution:

	def shortestUnSub(self, S, T):
		(n, m) = (len(S), len(T))
		dp = [[inf for j in range(m + 1)] for i in range(n + 1)]
		for i in range(1, n + 1):
			dp[i][0] = 1
		for i in range(1, n + 1):
			for j in range(1, m + 1):
				k = T[:j].rfind(S[i - 1])
				if k == -1:
					dp[i][j] = 1
				else:
					dp[i][j] = min(dp[i - 1][j], dp[i - 1][k] + 1)
		return dp[n][m] if dp[n][m] != inf else -1
