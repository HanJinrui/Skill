from math import factorial as fact

class Solution:

	def findCatalan(self, n):
		return fact(2 * n) // (fact(n + 1) * fact(n))
