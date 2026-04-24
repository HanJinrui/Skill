class Solution:

	def maxAmount(self, arr, N):
		dp = [[0] * N for i in range(N)]
		for i in range(N):
			dp[i][i] = arr[i]
		for gap in range(1, N):
			i = 0
			while i + gap < N:
				j = i + gap
				dp[i][j] = max(arr[i] - dp[i + 1][j], arr[j] - dp[i][j - 1])
				i = i + 1
		return (sum(arr) + dp[0][N - 1]) // 2
