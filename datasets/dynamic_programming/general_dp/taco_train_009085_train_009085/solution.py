class Solution:

	def countPaths(self, N):
		res = (3 ** N + 3 * (-1) ** N) * 250000002 % 1000000007
		return int(res)
