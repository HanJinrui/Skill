import math
EPS = 1e-15

class Solution:

	def findMinValue(self, a, n):
		summ = 0
		for i in range(n):
			summ += math.log10(a[i]) + EPS
		x1 = summ / n + EPS
		res = math.pow(10.0, x1) + EPS
		return math.ceil(res + EPS)
