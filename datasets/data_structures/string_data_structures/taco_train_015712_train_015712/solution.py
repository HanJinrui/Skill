class Solution:

	def search(self, patt, s):
		a = []
		for i in range(len(s)):
			if s.startswith(patt, i):
				a.append(i + 1)
		return a
