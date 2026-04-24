class Solution:

	def spirallyTraverse(self, matrix, r, c):
		res = []
		while matrix:
			res += matrix.pop(0)
			matrix = list(zip(*matrix))[::-1]
		return res
