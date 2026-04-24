class Solution:

	def findUnique(self, a, n, k):
		a.sort()
		for i in a[::k]:
			if a.count(i) % k != 0:
				return i
		return 0
