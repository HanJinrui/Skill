class Solution:

	def subsequenceSum(self, s):
		c = 0
		for i in s:
			c += int(i) * 2 ** (len(s) - 1)
		return c
