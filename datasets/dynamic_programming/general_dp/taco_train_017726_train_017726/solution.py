class Solution:

	def maximizeTheCuts(self, n, x, y, z):
		dp = [float('-inf')] * (n + 1)
		dp[0] = 0
		for i in range(1, n + 1):
			maxc = float('-inf')
			for l in [x, y, z]:
				if i >= l:
					maxc = max(maxc, 1 + dp[i - l])
			dp[i] = maxc
		return max(dp[-1], 0)
