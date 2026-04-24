class Solution:

	def palindromicPartition(self, string):
		n = len(string)
		dp = [0 for _ in range(n + 1)]
		for i in range(n - 1, -1, -1):
			minCuts = float('inf')
			for j in range(i, n):
				if self.isPalindrome(string[i:j + 1]):
					cuts = 1 + dp[j + 1]
					minCuts = min(cuts, minCuts)
			dp[i] = minCuts
		return dp[0] - 1

	def isPalindrome(self, x):
		return x == x[::-1]
