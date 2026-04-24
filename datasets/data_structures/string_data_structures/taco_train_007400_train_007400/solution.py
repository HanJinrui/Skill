class Solution:

	def buildLowestNumber(self, S, N):
		s = []
		for x in S:
			while s and N and (s[-1] > x):
				s.pop()
				N -= 1
			s.append(x)
		while N:
			s.pop()
			N -= 1
		return int(''.join(s))
