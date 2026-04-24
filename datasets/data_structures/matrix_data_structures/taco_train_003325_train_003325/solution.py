import numpy

class Solution:

	def determinantOfMatrix(self, A, n):
		return int(round(numpy.linalg.det(A)))
