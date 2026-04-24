class Solution:

	def findDistance(self, x, m, n):
		q = []
		(m, n) = (len(x), len(x[0]))
		for i in range(m):
			for j in range(n):
				if x[i][j] == 'B':
					q.append((i, j, 0))
					x[i][j] = 0
				elif x[i][j] == 'W':
					x[i][j] = -1
		while q:
			(i, j, k) = q.pop(0)
			for (d, e) in ((i + 1, j), (i, j + 1), (i - 1, j), (i, j - 1)):
				if 0 <= d < m and 0 <= e < n and (x[d][e] == 'O'):
					x[d][e] = k + 1
					q.append((d, e, k + 1))
		for i in range(m):
			for j in range(n):
				if x[i][j] == 'O':
					x[i][j] = -1
		return x
