class Solution:

	def sortingCost(self, N, arr):
		d = {}
		for a in arr:
			d[a] = d.get(a - 1, 0) + 1
		return N - max(d.values())
