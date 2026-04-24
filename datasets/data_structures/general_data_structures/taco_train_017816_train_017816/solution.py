class Solution:

	def Solve(self, n, a):
		l = []
		for i in a:
			if a.count(i) > n / 3:
				l.append(i)
		l = set(l)
		if len(l) == 0:
			return [-1]
		return l
