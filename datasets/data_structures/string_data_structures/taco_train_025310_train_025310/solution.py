class Solution:

	def countChars(self, s):
		return list(map(len, s.split()))
