class Solution:

	def isSuperSimilar(self, n, m, mat, x):
		pos = 1
		for i in range(n):
			for j in range(m):
				if mat[i][(j + x) % m] != mat[i][j]:
					pos = 0
					break
		return pos
