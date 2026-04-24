class Solution:

	def pairCount(self, N, A, B, C):
		count = 0
		for i in range(N):
			if A[i] - B[i] in C:
				count += 1
		return count
