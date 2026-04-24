class Solution:

	def firstNonRepeating(self, arr, n):
		hash = {}
		for i in arr:
			hash[i] = hash.get(i, 0) + 1
		for i in arr:
			if hash[i] == 1:
				return i
