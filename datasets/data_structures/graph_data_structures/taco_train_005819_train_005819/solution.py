from collections import deque
from typing import List

class Solution:

	def chefAndWells(self, n: int, m: int, c: List[List[str]]) -> List[List[int]]:
		dist = [[-1 for j in range(m)] for i in range(n)]
		Q = deque([(x, y) for x in range(n) for y in range(m) if c[x][y] == 'W'])
		for (x, y) in Q:
			dist[x][y] = 0
		while Q:
			(x, y) = Q.pop()
			for (nx, ny) in [(x, y + 1), (x, y - 1), (x + 1, y), (x - 1, y)]:
				if 0 <= nx < n and 0 <= ny < m and (dist[nx][ny] == -1) and (c[nx][ny] != 'N'):
					dist[nx][ny] = dist[x][y] + 2
					Q.appendleft((nx, ny))
		for x in range(n):
			for y in range(m):
				if c[x][y] in ['N', '.']:
					dist[x][y] = 0
		return dist
