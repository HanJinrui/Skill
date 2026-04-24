class Solution:

	def Addition(self, A, B):
		for i in range(len(A)):
			for j in range(len(A)):
				A[i][j] += B[i][j]
