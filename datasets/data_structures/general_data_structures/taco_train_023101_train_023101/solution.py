class Solution:

	def findIndex(self, a, N, key):
		first = -1
		last = -1
		if key in a:
			first = a.index(key)
			last = n - a[::-1].index(key) - 1
		return (first, last)
