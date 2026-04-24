from typing import List
from collections import deque

class Solution:

	def numberOfEnclaves(self, grid: List[List[int]]) -> int:
		ROWS = len(grid)
		COLS = len(grid[0])
		queue = deque()
		for i in range(ROWS):
			for j in range(COLS):
				if i == 0 or i == ROWS - 1 or j == 0 or (j == COLS - 1 and grid[i][j] == 1):
					queue.append([i, j])
		while queue:
			(x, y) = queue.popleft()
			if grid[x][y] == 0:
				continue
			grid[x][y] = 0
			for (i, j) in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
				if 0 <= x + i < ROWS and 0 <= y + j < COLS and (grid[x + i][y + j] == 1):
					queue.append([x + i, y + j])
		ans = 0
		for i in range(ROWS):
			for j in range(COLS):
				if grid[i][j] == 1:
					ans += 1
		return ans
