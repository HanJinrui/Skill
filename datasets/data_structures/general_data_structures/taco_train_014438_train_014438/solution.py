from itertools import accumulate

class Solution:

	def maxOccured(self, L, R, N, maxx):
		pr = [0] * (maxx + 2)
		for (i, j) in zip(L, R):
			pr[i] += 1
			pr[j + 1] -= 1
		a = list(accumulate(pr))
		return a.index(max(a))
