from math import factorial as fact

class Solution:

	def findRank(self, S):
		l = sorted(S)
		n = len(l)
		c = 0
		for i in range(n):
			d = l.index(S[i])
			c += d * fact(n - (i + 1))
			l.remove(l[d])
		return c + 1
