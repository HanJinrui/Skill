class Solution:

	def EqualString(self, s, t):
		if sorted(s[0::2]) == sorted(t[0::2]) and sorted(s[1::2]) == sorted(t[1::2]):
			return 1
		return 0
