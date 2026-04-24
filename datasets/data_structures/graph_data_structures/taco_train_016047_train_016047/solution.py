import sys
sys.setrecursionlimit(10 ** 8)

class Solution:

	def numIslands(self, grid):
		islands = 0
		for r in range(len(grid)):
			for c in range(len(grid[0])):
				if grid[r][c] == 1:
					islands += 1
					self.dfs(grid, r, c)
		return islands

	def dfs(self, grid, row, col):
		for r in range(row - 1, row + 2):
			for c in range(col - 1, col + 2):
				if r >= 0 and r < len(grid) and (c >= 0) and (c < len(grid[0])):
					if grid[r][c] == 1:
						grid[r][c] = 0
						self.dfs(grid, r, c)
