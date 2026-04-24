from math import factorial as fact

class Solution:

	def numberOfPaths(self, m, n):
		return fact(m + n - 2) // (fact(n - 1) * fact(m - 1)) % (10 ** 9 + 7)
