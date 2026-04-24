class Solution:

	def maxLevel(self, h, m):
		dp = {}

		def gameScore(h, m):
			if h <= 0 or m <= 0:
				return 0
			if (h, m) in dp:
				return dp[h, m]
			dp[h, m] = max(gameScore(h - 2, m - 8) + 2, gameScore(h - 17, m + 7) + 2)
			return dp[h, m]
		return gameScore(h, m) - 1
