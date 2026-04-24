class Solution:

	def rotateArr(self, A, D, N):
		if D > N:
			D = D % N
		A[:] = A[D:] + A[:D]
