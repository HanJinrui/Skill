class Solution:

	def isEularCircuitExist(self, V, adj):
		even = 0
		for i in adj:
			even += len(i) % 2
		if even == 2:
			return 1
		if even == 0:
			return 2
		return 0
