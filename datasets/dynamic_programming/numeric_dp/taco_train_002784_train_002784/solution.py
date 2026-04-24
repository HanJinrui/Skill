class Solution:

	def equalPartition(self, N, nums):
		sum_ = sum(nums)
		if sum_ % 2 != 0:
			return False
		half = sum_ // 2
		dp = [False] * (half + 1)
		dp[0] = True
		for el in nums:
			for j in range(half, el - 1, -1):
				if dp[j - el]:
					dp[j] = True
		return dp[half]
