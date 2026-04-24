class Solution:

	def minCoins(self, coins, M, V):
		dp = [V + 1] * (V + 1)
		dp[0] = 0
		for a in range(1, V + 1):
			for c in coins:
				if a - c >= 0:
					dp[a] = min(dp[a], 1 + dp[a - c])
		return dp[V] if dp[v] != V + 1 else -1
