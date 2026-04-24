class Solution:

	def countWays(self, n, Sum):
		mod = 10 ** 9 + 7
		dp = [[0] * max(10, Sum + 1) for _ in range(n + 1)]
		dp[0][0] = 1
		for j in range(1, 10):
			dp[1][j] = 1
		for i in range(2, n + 1):
			for j in range(1, Sum + 1):
				ans = 0
				for k in range(10):
					if j >= k:
						ans += dp[i - 1][j - k]
				dp[i][j] = ans % mod
		ans = dp[n][Sum]
		return ans if ans else -1
