class Solution:

	def SolveQueris(self, str, Query):
		return [len(set(str[q[0] - 1:q[1]])) for q in Query]
