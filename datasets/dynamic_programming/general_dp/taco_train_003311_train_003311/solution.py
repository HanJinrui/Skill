class Solution:

	def minStepToDeleteString(self, s):
		cache = {}

		def dp(i, j):
			if (i, j) in cache:
				return cache[i, j]
			if i > j:
				cache[i, j] = 0
				return cache[i, j]
			if i == j:
				cache[i, j] = 1
				return cache[i, j]
			cache[i, j] = float('inf')
			for k in range(i, j + 1):
				if s[i] == s[k]:
					temp = 1 + dp(k + 1, j) if k - i <= 1 else dp(i + 1, k - 1) + dp(k + 1, j)
					cache[i, j] = min(cache[i, j], temp)
			return cache[i, j]
		return dp(0, len(s) - 1)
