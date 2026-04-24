from functools import lru_cache

class Solution:

	def solve(self, n, m, grid):
		(R, C) = (n, m)

		@lru_cache(None)
		def dfs(r=0, c1=0, c2=C - 1):
			if r == R:
				return 0
			cherr = grid[r][c1] + (0 if c1 == c2 else grid[r][c2])
			ans = 0
			for nc1 in range(c1 - 1, c1 + 2):
				for nc2 in range(c2 - 1, c2 + 2):
					if 0 <= nc1 < C and 0 <= nc2 < C:
						ans = max(ans, dfs(r + 1, nc1, nc2))
			return ans + cherr
		return dfs()
