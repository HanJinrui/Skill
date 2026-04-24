class Solution:

	def min_operations(self, nums):
		N = len(nums)
		dp = [1] * N
		for i in range(1, N):
			for j in range(i):
				if nums[i] - nums[j] >= i - j:
					dp[i] = max(dp[i], dp[j] + 1)
		return N - max(dp)
