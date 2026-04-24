class Solution:

	def nthItem(self, L1, L2, A, B, N):
		s = {x + y for x in A for y in B}
		if len(s) < N:
			return -1
		return sorted(s)[N - 1]
