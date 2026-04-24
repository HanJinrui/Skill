class Solution:

	def isReversible(self, str, n):
		return int(str == str[::-1])
