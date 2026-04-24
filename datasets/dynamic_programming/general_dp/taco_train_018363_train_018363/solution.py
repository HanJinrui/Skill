class Solution:

	def LongestBitonicSequence(self, a):
		n = len(a)
		dp = [1] * n
		for ind in range(n):
			for prev in range(ind):
				if a[prev] < a[ind] and 1 + dp[prev] > dp[ind]:
					dp[ind] = 1 + dp[prev]
		maxi = 0
		dp2 = [1] * n
		for ind in range(n - 1, -1, -1):
			for prev in range(n - 1, ind, -1):
				if a[prev] < a[ind] and 1 + dp2[prev] > dp2[ind]:
					dp2[ind] = 1 + dp2[prev]
			maxi = max(maxi, dp[ind] + dp2[ind] - 1)
		return maxi
