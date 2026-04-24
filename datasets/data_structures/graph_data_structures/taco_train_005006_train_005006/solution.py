class Solution:

	def numberOfCells(self, n, m, r, c, u, d, mat):
		count = 0
		q = [(r, c, 0, 0)]
		mat[r][c] = '#'
		while q:
			(i, j, uu, dd) = q.pop(0)
			count += 1
			for (x, y) in [(0, +1), (0, -1), (-1, 0), (+1, 0)]:
				(xx, yy) = (i + x, j + y)
				if not (0 <= xx < n and 0 <= yy < m and (mat[xx][yy] == '.')):
					continue
				if x == +1 and dd + 1 <= d:
					q.append((xx, yy, uu, dd + 1))
					mat[xx][yy] = '#'
				elif x == -1 and uu + 1 <= u:
					q.append((xx, yy, uu + 1, dd))
					mat[xx][yy] = '#'
				elif x == 0:
					q.append((xx, yy, uu, dd))
					mat[xx][yy] = '#'
		return count
