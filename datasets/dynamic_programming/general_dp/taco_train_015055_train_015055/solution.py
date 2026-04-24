class Solution:

	def longestIncreasingPath(self, matrix, n, m):
		dp = [[-1] * m for i in range(n)]
		dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

		def dfs(i, j):
			if dp[i][j] != -1:
				return dp[i][j]
			dp[i][j] = 1
			for k in dirs:
				(i1, j1) = (i + k[0], j + k[1])
				if 0 <= i1 < n and 0 <= j1 < m:
					if matrix[i][j] > matrix[i1][j1]:
						dp[i][j] = max(dp[i][j], 1 + dfs(i1, j1))
			return dp[i][j]
		ans = 0
		for i in range(n):
			for j in range(m):
				ans = max(ans, dfs(i, j))
		return ans
