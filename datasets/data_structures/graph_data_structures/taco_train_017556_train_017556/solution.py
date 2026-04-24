class Solution:

	def isEularCircuitExist(self, n, adj):
		return all((len(i) % 2 == 0 for i in adj))
