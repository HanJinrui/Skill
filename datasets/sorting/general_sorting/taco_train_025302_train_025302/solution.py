class Solution:

	def findMinDiff(self, A, N, M):
		A.sort()
		return min([A[i + M - 1] - A[i] for i in range(N - M + 1)])
