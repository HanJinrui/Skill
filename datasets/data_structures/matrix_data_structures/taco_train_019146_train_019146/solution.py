class Solution:

	def rotate(self, matrix):
		matrix.reverse()
		for i in matrix:
			i.reverse()
