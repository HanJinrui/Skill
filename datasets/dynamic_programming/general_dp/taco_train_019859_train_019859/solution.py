import math
from functools import lru_cache

class Solution:

	def minDifference(self, nums, n):
		totalSum = sum(nums)

		@lru_cache(None)
		def dp(sum1, i):
			if i == -1:
				return abs(totalSum - 2 * sum1)
			ans = dp(sum1, i - 1)
			ans = min(ans, dp(sum1 + nums[i], i - 1))
			return ans
		return dp(0, n - 1)
