class Solution:

	def bitonic(self, arr, n):
		dp = [1] * n
		for i in range(1, n):
			if arr[i] >= arr[i - 1]:
				dp[i] = dp[i - 1] + 1
		dp2 = [1] * n
		for i in range(n - 2, -1, -1):
			if arr[i] >= arr[i + 1]:
				dp2[i] = dp2[i + 1] + 1
		ans = 0
		for i in range(n):
			ans = max(ans, dp[i] + dp2[i] - 1)
		return ans
