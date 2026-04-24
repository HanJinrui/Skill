class Solution:

	def getMin(self, A, B, n):
		l = []
		t = A.index(min(A))
		r = B.index(min(B))
		if t != r:
			return min(A) + min(B)
		for i in range(n):
			for j in range(n):
				if i != j:
					l.append(A[i] + B[j])
		if len(l) == 0:
			return -1
		return min(l)
