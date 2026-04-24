class Solution:

	def updateQuery(self, N, Q, U):
		count = [[0] * 17 for _ in range(N + 1)]
		for (l, r, x) in U:
			(l, r) = (l - 1, r - 1)
			for b in range(17):
				if x & 1 << b:
					count[l][b] += 1
					count[r + 1][b] -= 1
		for i in range(1, N):
			for j in range(17):
				count[i][j] += count[i - 1][j]
