from math import factorial

class Solution:

	def possibleStrings(ob, n, R, B, G):
		res = 0
		for r in range(R, n + 1):
			for g in range(G, n + 1):
				if n - (r + g) < B:
					continue
				res += factorial(n) // (factorial(r) * factorial(g) * factorial(n - r - g))
		return res
