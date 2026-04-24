class Solution:

	def maximumDifferenceSum(self, arr, N):
		dp = [[0] * 2 for i in range(N)]
		for i in range(1, N):
			dp[i][0] = max(dp[i - 1][0] + abs(arr[i] - arr[i - 1]), dp[i - 1][1] + abs(arr[i] - 1))
			dp[i][1] = max(dp[i - 1][0] + abs(1 - arr[i - 1]), dp[i - 1][1])
		return max(dp[-1])
