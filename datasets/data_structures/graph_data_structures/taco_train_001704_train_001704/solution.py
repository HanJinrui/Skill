import sys
sys.setrecursionlimit(10 ** 7)

class Solution:

	def countDistinctIslands(self, grid) -> int:

		def dfs(i, j, si, sj):
			if 0 <= i < len(grid) and 0 <= j < len(grid[0]) and (grid[i][j] == 1):
				grid[i][j] *= -1
				isl.append((i - si, j - sj))
				dirs = [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]
				for (ii, jj) in dirs:
					dfs(ii, jj, si, sj)
		isls = set()
		for i in range(len(grid)):
			for j in range(len(grid[0])):
				if grid[i][j] != 1:
					continue
				isl = []
				dfs(i, j, i, j)
				isls.add(tuple(isl))
		return len(isls)
