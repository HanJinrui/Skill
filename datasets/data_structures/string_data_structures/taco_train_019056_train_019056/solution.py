class Solution:

	def modified(self, s):
		k = 0
		i = 1
		while i < len(s) - 1:
			if s[i - 1] == s[i] and s[i] == s[i + 1]:
				k += 1
				i += 1
			i += 1
		return k
