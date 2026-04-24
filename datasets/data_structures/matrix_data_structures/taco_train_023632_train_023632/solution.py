class Solution:

	def BoundaryElements(self, M):
		L = []
		n = len(M)
		for i in range(n):
			for j in range(n):
				if (i == 0 or i == n - 1) or (j == 0 or j == n - 1):
					L.append(M[i][j])
		return L
