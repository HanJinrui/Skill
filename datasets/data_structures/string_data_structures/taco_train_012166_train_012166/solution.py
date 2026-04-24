class Solution:

	def maximum_distance(self, s):
		a = set()
		a.add('a')
		m = -1
		for i in range(len(s)):
			if chr(ord(s[i]) - 1) in a:
				a.add(s[i])
				m = max(m, i + 1)
		return m
