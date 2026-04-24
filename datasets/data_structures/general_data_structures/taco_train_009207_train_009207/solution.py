class Solution:

	def countPairsWithDiffK(self, arr, n, k):
		arr.sort()
		m = {}
		c = 0
		for i in arr:
			if i - k in m:
				c += m[i - k]
			if i not in m:
				m[i] = 1
			else:
				m[i] += 1
		return c
