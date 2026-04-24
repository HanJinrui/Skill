class Solution:

	def isGoodString(self, s):
		for i in range(len(s) - 1):
			if s[i] == s[i + 1]:
				return 'NO'
		return 'YES'
