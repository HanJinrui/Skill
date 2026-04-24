class Solution:

	def countWays(self, S1, S2):

		def solve(i, j):
			if j == len(S2):
				return 1
			if i >= len(S1):
				return 0
			if S1[i] == S2[j]:
				return solve(i + 1, j + 1) + solve(i + 1, j)
			else:
				return solve(i + 1, j)
		return solve(0, 0)
