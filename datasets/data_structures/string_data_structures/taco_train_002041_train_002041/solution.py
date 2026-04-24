class Solution:

	def longestSubstrDistinctChars(self, S):
		maxi = 0
		l = []
		for i in S:
			while i in l:
				l.remove(l[0])
			l.append(i)
			if maxi < len(l):
				maxi = len(l)
		return maxi
