class Solution:

	def telephoneNum(self, n):
		mod = 10 ** 9 + 7
		dp = [0] * max(n + 1, 5)
		dp[1] = 1
		dp[2] = 2
		for i in range(3, n + 1):
			dp[i] = (dp[i - 1] + (i - 1) * dp[i - 2]) % mod
		return dp[n]
