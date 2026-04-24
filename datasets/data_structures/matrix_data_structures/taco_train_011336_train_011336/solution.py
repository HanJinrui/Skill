class Solution:

	def Mutliply(self, matrixA, matrixB):
		import numpy as np
		x = np.array(matrixA)
		y = np.array(matrixB)
		matrixA[:] = np.dot(x, y)
		return matrixA
