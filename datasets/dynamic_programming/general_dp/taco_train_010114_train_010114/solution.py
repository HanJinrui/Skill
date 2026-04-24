class Solution:

	def solveWordWrap(self, nums, k):
		n = len(nums)
		dp = [float('INF')] * n
		dp[-1] = 0
		for i in range(n - 2, -1, -1):
			currlen = -1
			for j in range(i, n):
				currlen += nums[j] + 1
				if currlen > k:
					break
				if j == n - 1:
					dp[i] = 0
				else:
					dp[i] = min(dp[i], (k - currlen) ** 2 + dp[j + 1])
		return dp[0]
