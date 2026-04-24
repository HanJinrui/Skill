class Solution:

	def maxCoins(self, arr, n):
		dp = [[0] * (n + 2) for _ in range(n + 2)]
		for i in range(n):
			dp[i][i] = arr[i]
		for i in range(n - 1, -1, -1):
			for j in range(n):
				if i < j:
					dp[i][j] = max(arr[i] + min(dp[i + 1][j - 1], dp[i + 2][j]), arr[j] + min(dp[i][j - 2], dp[i + 1][j - 1]))
		return dp[0][n - 1]
