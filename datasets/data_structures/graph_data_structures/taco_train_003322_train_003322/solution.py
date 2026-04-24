class Solution:

	def helpaterp(self, x):
		(m, n) = (len(x), len(x[0]))
		q = []
		for i in range(m):
			for j in range(n):
				if x[i][j] == 2:
					q.append((i, j, 0))
		ma = 0
		while q:
			(i, j, k) = q.pop(0)
			ma = max(ma, k)
			for (d, e) in ((i + 1, j), (i, j + 1), (i - 1, j), (i, j - 1)):
				if 0 <= d < m and 0 <= e < n and (x[d][e] == 1):
					q.append((d, e, k + 1))
					x[d][e] = 2
		return ma if all((all((x[i][j] != 1 for j in range(n))) for i in range(m))) else -1
