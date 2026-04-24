class Solution:

	def shortestDistance(self, row, col, grid, tarX, tarY):
		if not grid[0][0] or not grid[tarX][tarY]:
			return -1
		q = []
		q.append((0, 0, 0))
		grid[0][0] = 0
		for (i, j, d) in q:
			if i == tarX and j == tarY:
				return d
			for (x, y) in [[i - 1, j], [i + 1, j], [i, j + 1], [i, j - 1]]:
				if 0 <= x < row and 0 <= y < col and grid[x][y]:
					grid[x][y] = 0
					q.append((x, y, d + 1))
		return -1
