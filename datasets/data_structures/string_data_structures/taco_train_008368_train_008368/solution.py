class Solution:

	def firstNonRepeating(self, a, n):
		d = {}
		for i in range(n):
			d[a[i]] = i
		return a[min(d.values())]
