import numpy

class Solution:

	def kroneckerProduct(self, n, m, p, q, A, B):
		kronecker = numpy.kron(A, B)
		return kronecker
