class Solution:

	def getMaxOccurringChar(self, s):
		s = sorted(s)
		return sorted(s, key=lambda x: s.count(x), reverse=True)[0]
