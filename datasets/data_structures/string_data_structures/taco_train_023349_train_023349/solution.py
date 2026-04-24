class Solution:

	def addMinChar(self, str1):
		n = len(str1)
		s = str1[::-1]
		x = str1[0]
		for i in range(n):
			if s[i] == x:
				if str1[0:n - i] == s[i:]:
					return i
		return n - 1
