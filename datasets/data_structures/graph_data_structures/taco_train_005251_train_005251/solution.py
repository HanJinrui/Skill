class Solution:

	def detectCycle(self, V, adj):
		s = set()
		for i in adj:
			l1 = len(s)
			l2 = len(i)
			s = s.union(i)
			if len(s) != l1 + l2:
				return 1
		return 0
