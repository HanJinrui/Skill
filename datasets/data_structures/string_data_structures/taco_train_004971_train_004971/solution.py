from math import factorial

class Solution:

	def mapStr(ob, N):
		return factorial(N) % (10 ** 9 + 7)
