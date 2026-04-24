class Solution:

	def sumExists(self, arr, n, target):
		setti = set()
		for item in arr:
			if target - item in setti:
				return 1
			setti.add(item)
		return 0
