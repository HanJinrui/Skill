class Solution:

	def nonRepetitive(self, s):
		d = {}
		n = len(s)
		for i in range(n):
			if s[i] in d:
				if i - d[s[i]] > 1:
					return 0
			d[s[i]] = i
		return 1
