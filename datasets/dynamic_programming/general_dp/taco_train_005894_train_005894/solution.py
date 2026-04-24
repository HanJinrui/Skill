class Solution:

	def numberOfPermWithKInversion(self, N, K):
		(List1, List2) = (K + 1, N + 1)
		dp = [[0 for I in range(List1)] for j in range(List2)]
		for i in range(1, N + 1):
			dp[i][0] = 1
		for i in range(1, N + 1):
			for j in range(1, K + 1):
				val = dp[i - 1][j]
				if j >= i:
					val -= dp[i - 1][j - i]
				dp[i][j] = dp[i][j - 1] + val
		ans = dp[N][K]
		if K >= 1:
			ans -= dp[N][K - 1]
		return ans % 1000000007
