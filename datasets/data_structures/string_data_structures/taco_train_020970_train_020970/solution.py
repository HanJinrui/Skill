class Solution:

	def encryptString(self, s):
		i = 0
		res = ''
		while i < len(s):
			res += s[i]
			c = 0
			while i < len(s) and s[i] == res[-1]:
				c += 1
				i += 1
			res += str(c)
		return res[::-1]
