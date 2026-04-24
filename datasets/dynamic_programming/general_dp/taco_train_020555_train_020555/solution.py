from math import factorial

class Solution:

	def NumberOfPaths(self, a, b):
		return factorial(a + b - 2) // factorial(a - 1) // factorial(b - 1)
