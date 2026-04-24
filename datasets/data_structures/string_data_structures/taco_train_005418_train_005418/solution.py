class Solution:

	def search(self, pat, txt):
		lis = []
		pos = txt.find(pat)
		while pos >= 0:
			lis.append(pos + 1)
			pos = txt.find(pat, pos + 1)
		return lis
