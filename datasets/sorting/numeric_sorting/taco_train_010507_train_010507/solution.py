class Solution:

	def MaxSum(self, A, B, N):
		A.sort()
		B.sort()
		return sum((A[i] * B[i] for i in range(N)))
