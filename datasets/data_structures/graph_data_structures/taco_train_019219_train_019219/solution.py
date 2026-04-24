class Solution:

	def isNegativeWeightCycle(self, n, edges):
		d = [0 for i in range(n)]
		for i in range(n):
			relaxed = False
			for e in edges:
				if d[e[0]] + e[2] < d[e[1]]:
					d[e[1]] = d[e[0]] + e[2]
					relaxed = True
		if relaxed == False:
			return 0
		return 1
