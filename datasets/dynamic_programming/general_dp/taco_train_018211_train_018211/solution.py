class Solution:

	def eggDrop(self, n, k):
		dp = [0] * (n + 1)
		m = 0
		while dp[n] < k:
			m += 1
			for x in range(n, 0, -1):
				dp[x] += 1 + dp[x - 1]
		return m
