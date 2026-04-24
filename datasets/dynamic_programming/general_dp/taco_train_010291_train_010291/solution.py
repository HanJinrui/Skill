class Solution:

	def countWays(self, N, S):
		d1 = dict()

		def dfs(i, j):
			if i == j:
				if S[i] == 'T':
					return (1, 0)
				else:
					return (0, 1)
			if d1.get((i, j)) != None:
				return d1[i, j]
			(T, F) = (0, 0)
			for k in range(i + 1, j, 2):
				(a, b) = dfs(i, k - 1)
				(c, d) = dfs(k + 1, j)
				if S[k] == '|':
					T = T + a * c + a * d + b * c
					F = F + b * d
				if S[k] == '&':
					T = T + a * c
					F = F + b * c + a * d + b * d
				if S[k] == '^':
					T = T + a * d + c * b
					F = F + a * c + b * d
			d1[i, j] = (T, F)
			return (T, F)
		(a, b) = dfs(0, N - 1)
		return a % 1003
