from collections import deque

class Solution:

	def nearest(self, grid):
		m = len(grid)
		n = len(grid[0])
		vs = [[0] * n for _ in range(m)]
		q = deque()
		for i in range(m):
			for j in range(n):
				if grid[i][j] == 1:
					q.append((i, j, 0))
					vs[i][j] = 1
					grid[i][j] = 0
		dx = [-1, 0, 1, 0]
		dy = [0, 1, 0, -1]
		while len(q) > 0:
			rp = q.popleft()
			for i in range(4):
				nx = rp[0] + dx[i]
				ny = rp[1] + dy[i]
				if nx >= 0 and nx < m and (ny >= 0) and (ny < n) and (vs[nx][ny] == 0) and (grid[nx][ny] == 0):
					grid[nx][ny] = rp[2] + 1
					vs[nx][ny] = 1
					q.append((nx, ny, rp[2] + 1))
		return grid
