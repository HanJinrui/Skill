from collections import defaultdict

class Solution:

	def MaximumSum(self, a, n):
		if n == 1:
			return 0
		store = defaultdict(lambda : 0)
		for item in a:
			store[item] += 1
		maxi = max(store.keys())
		if store[maxi] > 1:
			return store[maxi] * (store[maxi] - 1) // 2
		del store[maxi]
		return store[max(store.keys())]
