class Solution:

	def is_Possible(self, grid):
		m = len(grid)
		n = len(grid[0])
		vis = set()

		def bfs(r, c):
			if r < 0 or r == m or c < 0 or (c == n) or (grid[r][c] == 0) or ((r, c) in vis):
				return 0
			if grid[r][c] == 2:
				return 1
			vis.add((r, c))
			return bfs(r + 1, c) or bfs(r - 1, c) or bfs(r, c + 1) or bfs(r, c - 1)
		for i in range(m):
			for j in range(n):
				if grid[i][j] == 1:
					return bfs(i, j)
