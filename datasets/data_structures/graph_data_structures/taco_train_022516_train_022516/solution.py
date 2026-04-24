class Solution:

	def maximumMatch(self, G):
		return min(len(G), len(G[0]))
