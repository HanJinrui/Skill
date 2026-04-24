import numpy as np

class Solution:

	def ValidCorner(self, M):
		(R, C) = (len(M), len(M[0]))
		A = np.array(M)
		B = A.transpose()
		if C < R:
			(A, B, R, C) = (B, A, C, R)
		mul = A @ B - np.eye(R) * C
		return np.any(mul >= 2)
