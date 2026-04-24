class Solution:

	def check(self, n, l=[]):
		if n in l:
			return n == 1
		q = sum([int(x) ** 2 for x in str(n)])
		return self.check(q, [*l, n])

	def nextHappy(self, N):
		while True:
			N += 1
			if self.check(N):
				return N
