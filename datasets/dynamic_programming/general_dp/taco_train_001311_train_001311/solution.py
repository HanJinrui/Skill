from functools import lru_cache

class Solution:

	def perfectSum(self, arr, n, sum):
		mod = 10 ** 9 + 7
		dp = [0] * (sum + 1)
		dp[0] = 1
		for element in arr:
			for j in range(sum, element - 1, -1):
				dp[j] = (dp[j] + dp[j - element]) % mod
		return dp[sum] % mod
