from functools import lru_cache

class Solution:

	def findProb(self, n, r, c, k):
		dir = [(-1, -2), (-2, -1), (-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2)]

		@lru_cache(None)
		def solve(x, y, t):
			if not (0 <= x < n and 0 <= y < n):
				return 0
			if t == 0:
				return 1
			ans = 0
			for (i, j) in dir:
				ans += solve(x + i, y + j, t - 1)
			return ans
		return solve(r, c, k) / 8 ** k
