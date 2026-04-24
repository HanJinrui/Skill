class Solution:

	def diagonalSumDifference(self, N, Grid):
		import numpy as np
		matrix = np.array(Grid)
		return abs(matrix.trace() - matrix[::-1].trace())
