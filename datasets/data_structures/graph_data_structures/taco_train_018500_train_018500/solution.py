class Solution:

	def xShape(self, grid):
		n = len(grid)
		m = len(grid[0])

		def dfs(i, j):
			if i < 0 or i > n - 1 or j < 0 or (j > m - 1) or (grid[i][j] != 'X'):
				return
			grid[i][j] = '2'
			dfs(i + 1, j)
			dfs(i - 1, j)
			dfs(i, j - 1)
			dfs(i, j + 1)
		cnt = 0
		for i in range(n):
			for j in range(m):
				if grid[i][j] == 'X':
					dfs(i, j)
					cnt += 1
		return cnt
