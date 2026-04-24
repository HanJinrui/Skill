class Solution:

	def getPairsCount(self, arr, n, k):
		d = {}
		count = 0
		for i in arr:
			if k - i in d:
				count += d[k - i]
			d[i] = d.get(i, 0) + 1
		return count
