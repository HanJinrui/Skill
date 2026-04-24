class Solution:

	def sequence(self, N):
		i = 1
		s = 0
		for n in range(1, N + 1):
			cur = 1
			for _ in range(n):
				cur *= i
				i += 1
			s += cur
		return s
