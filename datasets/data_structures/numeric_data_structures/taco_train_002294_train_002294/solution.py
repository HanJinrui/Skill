class Solution:

	def factorial(self, a, n):
		m = max(a)
		f = [1]
		for i in range(1, m + 1):
			f.append(f[-1] * i % (10 ** 9 + 7))
		res = []
		for i in a:
			res.append(f[i])
		return res
