class Solution:

	def isSubsetSum(self, N, arr, sum):
		dp = [False] * (sum + 1)
		dp[0] = True
		for element in arr:
			for j in range(sum, element - 1, -1):
				if dp[j - element]:
					dp[j] = True
		return dp[-1]
