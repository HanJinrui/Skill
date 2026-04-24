class Solution:

	def getMaxWeight(self, s):
		n = len(s)
		dp = [0] * (n + 1)
		dp[1] = 1
		for i in range(2, n + 1):
			if s[i - 1] == s[i - 2]:
				dp[i] = max(dp[i - 2] + 3, dp[i - 1] + 1)
			else:
				dp[i] = dp[i - 2] + 4
		return dp[n]
