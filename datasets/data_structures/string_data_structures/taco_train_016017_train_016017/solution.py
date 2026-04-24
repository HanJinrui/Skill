class Solution:

	def StringQuery(self, N, Q, S, Q1, Q2):
		f = 0
		g = []
		for i in range(Q):
			if Q1[i] == 1:
				f = (f + (N - Q2[i])) % N
			else:
				g.append(S[(f + Q2[i]) % N])
		return g
