class Solution:

	def klengthpref(self, arr, n, k, s):
		ct = 0
		for ar in arr:
			if s[:k] == ar[:k]:
				ct += 1
		return ct
