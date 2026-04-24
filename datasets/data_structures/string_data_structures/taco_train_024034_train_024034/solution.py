class Solution:

	def convertToEven(self, s):
		l = list(s.split('E'))
		ans = len(l) - l.count('')
		return ans
