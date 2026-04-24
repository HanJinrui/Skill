class Solution:

	def solve(self, a, b, c):
		l = [a, b, c]
		l.sort()
		if l[-1] >= 3 + 2 * (l[0] + l[1]):
			return -1
		return a + b + c
