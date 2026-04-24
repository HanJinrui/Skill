from collections import Counter

class Solution:

	def getTwinCount(self, N, Arr):
		a = Counter(Arr)
		out = 0
		for i in a.values():
			out += i // 2
		return out * 2
