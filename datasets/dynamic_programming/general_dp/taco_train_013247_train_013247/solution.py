class Solution:

	def knapSack(self, n, size, value, weight):
		dp = [0] * (size + 1)
		for i in range(1, n + 1):
			for j in range(weight[i - 1], size + 1):
				dp[j] = max(dp[j], dp[j - weight[i - 1]] + value[i - 1])
		return dp[size]
