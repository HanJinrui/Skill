from bisect import bisect_right

class Solution:

	def findSurpasser(self, a, n):
		b = [0] * n
		l = [a[n - 1]]
		for i in range(n - 2, -1, -1):
			j = bisect_right(l, a[i])
			b[i] = len(l) - j
			l.insert(j, a[i])
		return b
