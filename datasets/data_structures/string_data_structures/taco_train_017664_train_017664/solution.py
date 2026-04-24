class Solution:

	def isRepeat(self, s):
		return int(s in (2 * s)[1:-1])
