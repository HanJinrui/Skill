class Solution:

	def optimalWalk(self, N, A, B):
		dp = [0 for i in range(N + 1)]
		dp[1] = A
		for i in range(2, N + 1):
			dp[i] = min(A + dp[i - 1], dp[(i + 1) // 2] + B + i % 2 * A)
		return dp[N]
