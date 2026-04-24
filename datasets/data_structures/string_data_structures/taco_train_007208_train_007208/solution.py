class Solution:

	def countZero(self, n, k, arr):
		(l, r) = (set(), set())
		res = []
		for (i, j) in arr:
			l.add(i)
			r.add(j)
			res.append((n - len(l)) * (n - len(r)))
		return res
