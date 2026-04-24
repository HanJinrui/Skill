class Solution:

	def findMaxArea(self, grid):

		def fun(i, j):
			if i < 0 or i > row - 1 or j < 0 or (j > col - 1):
				return 0
			if grid[i][j] == 0:
				return 0
			c = 1
			grid[i][j] = 0
			for a in range(i - 1, i + 2, 1):
				for b in range(j - 1, j + 2, 1):
					c += fun(a, b)
			return c
		row = len(grid)
		col = len(grid[0])
		x = []
		for i in range(row):
			for j in range(col):
				if grid[i][j] == 1:
					x.append(fun(i, j))
		return max(x) if x else 0
