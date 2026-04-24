class Solution:

	def minimumInteger(self, N, A):
		A.sort()
		s = sum(A)
		for i in range(0, N):
			if s <= A[i] * N:
				return A[i]
