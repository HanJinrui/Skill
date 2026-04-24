class Solution:

	def minRow(self, N, M, A):
		return min(range(N), key=lambda x: sum(A[x])) + 1
