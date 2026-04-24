from functools import lru_cache

class Solution:

	def lcs(self, x, y, s1, s2):

		@lru_cache(None)
		def dp(i, j):
			if i == x or j == y:
				return 0
			if s1[i] == s2[j]:
				return 1 + dp(i + 1, j + 1)
			else:
				return max(dp(i, j + 1), dp(i + 1, j))
		return dp(0, 0)
