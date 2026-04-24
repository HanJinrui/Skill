class Solution:

	def binaryAdd(self, n, s):
		return str(bin(int(s, 2) + 1))[2:].zfill(len(s))
