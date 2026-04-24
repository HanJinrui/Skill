class Solution:

	def findPairs(self, arr, n):
		hash = set()
		res = []
		for el in arr:
			if -el in hash:
				res += sorted([el, -el])
			hash.add(el)
		return res
