class Solution:

	def count(self, N, M):
		dp = [[0 for i in range(M + 5)] for i in range(0, N + 5)]
		for i in range(1, M + 1):
			dp[1][i] = 1
		MOD = 10 ** 9 + 7
		for i in range(2, N + 2):
			for j in range(1, M + 1):
				for k in range(j, M + 1, j):
					dp[i][k] = (dp[i][k] + dp[i - 1][j]) % MOD
					if j == k:
						continue
					dp[i][j] = (dp[i][j] + dp[i - 1][k]) % MOD
		ans = 0
		for i in range(1, M + 1):
			ans = (ans + dp[N][i]) % MOD
		return ans
