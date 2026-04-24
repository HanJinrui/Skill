class Solution:

	def isRotatedPalindrome(self, s):
		d = {}
		for ch in s:
			if ch in d.keys():
				d.pop(ch)
			else:
				d[ch] = 1
		if len(d) > 1:
			return 0
		else:
			return 1
