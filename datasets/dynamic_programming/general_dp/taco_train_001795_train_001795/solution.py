import sys

class Solution:

	def minimumCost(self, cost, n, W):
		dp = [float('inf')] * (W + 1)
		dp[0] = 0
		for i in range(n):
			if cost[i] == -1:
				continue
			for j in range(1, W + 1):
				if j >= i + 1:
					dp[j] = min(dp[j], cost[i] + dp[j - (i + 1)])
		return dp[-1]
