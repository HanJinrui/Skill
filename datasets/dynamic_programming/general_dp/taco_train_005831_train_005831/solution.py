class Solution:

	def maxCalories(self, arr, n):
		if n < 3:
			return sum(arr)
		dp = [0 for i in range(n)]
		dp[0] = arr[0]
		dp[1] = arr[0] + arr[1]
		dp[2] = max(dp[1], arr[2] + dp[0], arr[2] + arr[1])
		for i in range(3, n):
			dp[i] = max(dp[i - 1], arr[i] + dp[i - 2], arr[i] + arr[i - 1] + dp[i - 3])
		return dp[n - 1]
