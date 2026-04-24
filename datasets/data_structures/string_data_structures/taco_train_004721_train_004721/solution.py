class Solution:

	def evenNumSubstring(self, s):
		l = []
		for i in range(len(s)):
			if int(s[i]) % 2 == 0:
				l.append(i + 1)
		return sum(l)
