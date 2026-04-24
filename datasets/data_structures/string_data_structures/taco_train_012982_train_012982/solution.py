class Solution:

	def isSame(self, s):
		for x in range(len(s)):
			if s[x].isdigit():
				return int(len(s[:x]) == int(s[x:]))
