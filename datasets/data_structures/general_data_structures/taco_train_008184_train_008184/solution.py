class Solution:

	def printMissingIntervals(self, a, n):
		s = 0
		res = []
		for x in a:
			if x > s:
				res += [s, x - 1]
			s = x + 1
		if s <= 99999:
			res += [s, 99999]
		return res
