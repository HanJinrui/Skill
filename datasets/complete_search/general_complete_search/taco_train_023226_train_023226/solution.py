class Solution:

	def increasingNumbers(self, N):
		l = []

		def f(dig, last):
			if len(dig) == N:
				if not (len(dig) > 1 and dig[0] == '0'):
					l.append(dig)
			for i in range(last + 1, 10):
				f(dig + str(i), i)
		f('', -1)
		return l
