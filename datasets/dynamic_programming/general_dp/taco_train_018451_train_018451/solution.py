class Solution:

	def FindWays(self, n, m, blocked_cells):
		dp = {}
		dp[1, 1] = 1
		for (a, b) in blocked_cells:
			dp[a, b] = 0

		def dfs(n, m):
			if (n, m) in dp:
				return dp[n, m]
			if n < 1 or m < 1:
				dp[n, m] = 0
				return 0
			dp[n, m] = dfs(n - 1, m) + dfs(n, m - 1)
			return dp[n, m]
		return dfs(n, m) % (10 ** 9 + 7)
