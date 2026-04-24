class Solution:

	def matrixDiagonally(self, mat):
		r = c = len(mat)
		res = [[] for i in range(c + r - 1)]
		for i in range(r):
			for j in range(c):
				s = i + j
				if s % 2 == 0:
					res[s].insert(0, mat[i][j])
				else:
					res[s].append(mat[i][j])
		return sum(res, [])
