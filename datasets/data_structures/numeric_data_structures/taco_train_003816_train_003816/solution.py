class Solution:

	def numOfSubsets(self, x, n, k):
		dp = {}

		def f(i, j):
			if j > k:
				return 0
			if i == n:
				return 1
			if (i, j) in dp:
				return dp[i, j]
			dp[i, j] = f(i + 1, j) + f(i + 1, j * x[i])
			return dp[i, j]
		return f(0, 1) - 1
