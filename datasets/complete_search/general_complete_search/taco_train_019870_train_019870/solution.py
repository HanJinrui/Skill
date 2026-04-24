from itertools import permutations

class Solution:

	def uniquePerms(self, arr, n):
		return sorted(set(permutations(arr)))
