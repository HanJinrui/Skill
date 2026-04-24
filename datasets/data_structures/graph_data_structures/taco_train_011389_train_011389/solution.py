class Solution:

	def isPossible(self, paths):
		for i in range(len(paths)):
			temp = sum([1 for x in paths[i] if x == 1])
			if temp % 2 != 0:
				return 0
		return 1
