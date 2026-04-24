class Solution:

	def removeDups(self, s):
		r = ''
		for i in s:
			if i not in r:
				r = r + i
		return r
