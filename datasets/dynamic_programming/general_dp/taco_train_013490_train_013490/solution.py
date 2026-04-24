from functools import lru_cache

class Solution:

	@lru_cache(maxsize=1000000)
	def dp(self, m, n):
		ans = 10000000000
		if m == n:
			return 1
		for i in range(1, m):
			ans = min(ans, self.dp(i, n) + self.dp(m - i, n))
		for i in range(1, n):
			ans = min(ans, self.dp(m, i) + self.dp(m, n - i))
		return ans

	def minCut(self, M, N):
		return self.dp(M, N)
