class Solution:

	def firstRepChar(self, s):
		S = {}
		for i in s:
			if i in S:
				return i
			S[i] = 1
		return -1
