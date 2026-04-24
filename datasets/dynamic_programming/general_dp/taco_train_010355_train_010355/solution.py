class Solution:

	def longestIncreasingPath(self, x):
		(m, n) = (len(x), len(x[0]))

		def f(i, j):
			if (i, j) in dp:
				return dp[i, j]
			ans = 0
			for (d, e) in ((i + 1, j), (i, j + 1), (i - 1, j), (i, j - 1)):
				if 0 <= d < m and 0 <= e < n and (x[i][j] < x[d][e]):
					ans = max(ans, f(d, e))
			dp[i, j] = ans + 1
			return ans + 1
		dp = {}
		return max((max((f(i, j) for i in range(m))) for j in range(n)))
