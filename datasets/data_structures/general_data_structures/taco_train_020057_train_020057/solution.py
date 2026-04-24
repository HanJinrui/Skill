class Solution:

	def leaders(self, A, N):
		B = [A[-1]]
		for i in range(len(A) - 2, -1, -1):
			if A[i] >= B[-1]:
				B.append(A[i])
		return B[::-1]
