import collections

class Solution:

	def shotestPath(self, mat, m, n, k):
		(q, seen) = ([(0, 0, k, 0)], collections.defaultdict(lambda : -1))
		seen[0, 0] = k
		for (i, j, r, h) in q:
			if (i, j) == (m - 1, n - 1):
				return h
			if r < 0:
				continue
			for (x, y) in ((i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)):
				if m > x >= 0 <= y < n and seen[x, y] < r - mat[x][y]:
					seen[x, y] = r - mat[x][y]
					q += ((x, y, r - mat[x][y], h + 1),)
		return -1
