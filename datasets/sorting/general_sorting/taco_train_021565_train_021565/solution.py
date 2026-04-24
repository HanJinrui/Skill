import math

class Solution:

	def countPairs(self, a, b, M, N):

		def trans(x):
			return math.log2(x) / x
		b.sort(key=trans)
		a.sort(key=trans)
		k = 0
		j = 0
		for i in a:
			while j < N and trans(i) > trans(b[j]):
				j += 1
			k += j
		return k
