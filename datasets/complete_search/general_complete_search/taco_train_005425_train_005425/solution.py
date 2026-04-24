class Solution:

	def pattern(self, N):
		l = []
		while N > 0:
			l.append(N)
			N -= 5
		l += [N] + l[::-1]
		return l
