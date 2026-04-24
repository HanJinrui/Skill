class Solution:

	def removeAdj(self, v, n):
		s = []
		for i in v:
			if s and s[-1] == i:
				s.pop()
			else:
				s.append(i)
		return len(s)
