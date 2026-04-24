class Solution:

	def tiny_miny(self, a, n):
		res = []
		for i in range(1, n + 1):
			res.extend(list(str(a ** i)))
		res.sort()
		return int(''.join(res))
