class Solution:

	def minIndexChar(self, str, pat):
		for i in str:
			if i in pat:
				return str.index(i)
		return -1
