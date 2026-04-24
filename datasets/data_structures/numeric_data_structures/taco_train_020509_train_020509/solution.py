import math as m

class Solution:

	def findMin(self, a, n):
		summ = 0
		for i in range(n):
			summ += m.log(a[i])
		x = m.exp(summ / n)
		return int(x + 1)
