class Solution:

	def sumOfRowCol(self, N, M, A):
		A_T = list(map(list, zip(*A)))
		limit = min(N, M)
		for itr in range(limit):
			if sum(A[itr]) != sum(A_T[itr]):
				return 0
		return 1
