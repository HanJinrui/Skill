class Solution:

	def isPossible(self, S):
		s = set()
		i = 1
		while i <= len(S):
			if S[:i] not in s:
				s.add(S[:i])
				S = S[i:]
				i = 1
			else:
				i += 1
		return int(len(s) > 3)
