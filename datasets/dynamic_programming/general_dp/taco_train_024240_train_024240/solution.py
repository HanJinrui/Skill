class Solution:

	def distinctColoring(self, N, r, g, b):
		(rr, gg, bb) = (0, 0, 0)
		for i in range(N):
			ar = r[i] + min(gg, bb)
			ag = g[i] + min(rr, bb)
			ab = b[i] + min(rr, gg)
			(rr, gg, bb) = (ar, ag, ab)
		return min(rr, gg, bb)
