class Solution:

	def findAndReplace(self, S, q, ind, so, tar):
		ind.reverse()
		so.reverse()
		tar.reverse()
		for (i, s, t) in zip(index, sources, targets):
			if S[i:i + len(s)] == s:
				S = S[:i] + t + S[i + len(s):]
		return S
