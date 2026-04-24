class Solution:

	def satisfyEqn(self, A, N):
		for i in range(0, N):
			for j in range(0, N):
				for k in range(0, N):
					for l in range(0, N):
						if A[i] + A[j] == A[k] + A[l] and i != j and (k != l) and (j != k) and (i != k) and (j != l) and (i != l):
							return (i, j, k, l)
		return (-1, -1, -1, -1)
