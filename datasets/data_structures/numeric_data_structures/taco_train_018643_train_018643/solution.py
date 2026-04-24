class Solution:

	def maxPoint(self, N, K, A, B):
		return max([int(K / A[i]) * B[i] for i in range(len(A))])
